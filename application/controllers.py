from flask import Flask, request, flash, make_response
from flask import render_template, redirect, url_for
from flask import current_app as app
from application.models import *
from application.database import db
from application.config import basedir
from application.pygooglenews import GoogleNews
import json
import time
from tvDatafeed import TvDatafeed, Interval, TvDatafeedLive
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend("agg")
import os
from azure.storage.blob import BlobServiceClient






connect_str = "DefaultEndpointsProtocol=https;AccountName=frtprojectsa;AccountKey=dLR5paZToF0pqHMngNIluOL+c5IkUyWfx3m6pv78JrZrafDBLLVaRH8fMcu9Wh4bUq3ES4Yzijs++AStqLY8GA==;EndpointSuffix=core.windows.net"
container_name = "frt-project-container"


blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str)
container_client = blob_service_client.get_container_client(container_name)

@app.route("/", methods=["GET", "POST"])
def home(): 
    return render_template('home_page.html')



@app.route("/portfolio", methods=["GET", "POST"])
def portfolio(): 
    tvl = TvDatafeedLive()
    pe = Portfolio.query.all()
    p_e = []
    tpl = 0
    pi = {}
    for x in pe:
        live_data=tvl.get_hist(symbol=x.name,exchange='NSE',interval=Interval.in_5_minute,n_bars=10000,  extended_session=False, timeout=-1)
        cur_price = live_data["close"][-1]
        pl = 0
        if x.position == "Long":
            pl = x.price - cur_price
        elif x.position == "Short":
            pl = cur_price - x.price
        tpl += pl
        p_e.append([x.name,x.industry,x.position,pl])
        if x.industry in pi.keys():
            pi[x.industry] += int(x.price)
        else:
            pi[x.industry] = int(x.price)
    p_v = list(pi.values())
    plt.pie(np.array(p_v), labels = pi.keys(), autopct='%1.1f%%', startangle = 90, wedgeprops = {"edgecolor" : "black",'linewidth': 2,'antialiased': True})
    plt.axis('equal')
    
    plt.savefig(os.path.join(basedir, app.config['UPLOAD_FOLDER'], "port_div.png"))
    
    with open(file=os.path.join(basedir,app.config['UPLOAD_FOLDER'], 'port_div.png'), mode="rb") as data:
        container_client.upload_blob(name="port_div.png", data=data, overwrite=True)
       
    plt.close()
    os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], "port_div.png"))

    ######### Delete old ############
    ######### Upload to azure blob storage #############


    return render_template('port_folio.html',tpl=tpl,p_e=p_e)

@app.route("/news", methods=["GET", "POST"])
def news(): 
    L_new_s = LNews.query.all()
    S_new_s = SNews.query.all()


    return render_template('new_s.html',L_new_s=L_new_s, S_new_s=S_new_s)

@app.route("/aichatbot", methods=["GET", "POST"])
def aichatbot(): 
    return render_template('aichatbot.html')

@app.route("/refresh/news", methods=["GET", "POST"])
def refresh_news(): 
    gn = GoogleNews(lang = 'en', country = 'IN')
    L_new_s = []
    S_new_s = []
    lnd = LNews.query.delete()
    snd = SNews.query.delete()
    
    comps = Nifty.query.all()

    for x in comps:
        print(x.symbol)
        sd = gn.search(x.symbol,when='6h')
        ent = sd["entries"]
        
        for entry in ent:
            
            if "profit" in entry["title"].split(" ") or "high" in entry["title"].split(" ") or "hot" in entry["title"].split(" "):
                
                if (entry["title"] + entry["published"]) not in L_new_s:
                    
                    L_new_s.append([entry["title"] + entry["published"] , x.symbol])
                time.sleep(0.25)
                break
            elif "low" in entry["title"].split(" ") or "loss" in entry["title"].split(" ") or "down" in entry["title"].split(" "):
                if (entry["title"] + entry["published"] ) not in S_new_s: 
                    
                    S_new_s.append([entry["title"] + entry["published"] , x.symbol])
                time.sleep(0.25)
                break
    
    for i in range(len(L_new_s)):
        L_new_s[i][0] = (str(i+1)+". ") + L_new_s[i][0]
        lne = LNews(ln=L_new_s[i][0],ls=L_new_s[i][1]) 
        db.session.add(lne)
        db.session.commit()
    
    for i in range(len(S_new_s)):
        S_new_s[i][0] = (str(i+1)+". ") + S_new_s[i][0] 
        sne = SNews(sn=S_new_s[i][0],ss=S_new_s[i][1]) 
        db.session.add(sne)
        db.session.commit()

    return redirect(url_for('news'))


@app.route("/analyse/<symbol>", methods=["GET", "POST"])
def analyse(symbol): 
    
    tvl = TvDatafeedLive()
    tv = TvDatafeed()

    # index
    index_data = tv.get_hist(symbol=symbol,exchange='NSE',interval=Interval.in_1_minute,n_bars=10000,extended_session=False)
    live_data=tvl.get_hist(symbol=symbol,exchange='NSE',interval=Interval.in_5_minute,n_bars=10000,  extended_session=False, timeout=-1)
    
    print(live_data)
    ind = {}
    for i in range(len(live_data.index)):
        ind[i] = live_data.index[i]
    avg_vol = mean(live_data["volume"])
    count = 0
    for x in live_data["volume"]:
        if x < avg_vol:
            ind.pop(count)
        count += 1    
    print(avg_vol)
    past_data = []
    for i in range(len(live_data.index)):
       if abs(live_data["open"][i]-live_data["close"][i]) > (live_data["open"][i]*0.01):
           past_data.append([live_data.index[i],live_data["open"][i]-live_data["close"][i],live_data["volume"][i]])
    
    print(past_data)
    cur_vol = live_data["volume"][-1]
    cur_price = live_data["close"][-1]
    cur_change = live_data["open"][-1] - cur_price
    cur_trend = []
    for i in range(-3,0):
        cur_trend.append([live_data.index[i],live_data["open"][i]-live_data["close"][i],live_data["volume"][i]])
    
    tip = ""
    if cur_vol < avg_vol:
        tip = "Failed to meet the volume threshold."
    elif cur_change < (cur_price*0.03):
        tip = "Failed to meet the price action threshold."
    else:
        tip = "Passed volume and price action threshold."
    return render_template('ana_lyse.html',symbol=symbol,past_data=past_data,avg_vol=avg_vol,cur_vol=cur_vol,cur_price=cur_price,cur_change=cur_change,cur_trend=cur_trend,tip=tip)


@app.route("/buy/<symbol>/<buy_price>", methods=["GET", "POST"])
def buy(symbol,buy_price):
    ind = db.session.execute(db.select(Nifty.industry).filter_by(symbol=symbol)).scalar_one()
    npe = Portfolio(name=symbol,price=buy_price,position="Long",industry=ind)
    db.session.add(npe) 
    db.session.commit()

    return redirect(url_for('portfolio'))

@app.route("/sell/<symbol>/<sell_price>", methods=["GET", "POST"])
def sell(symbol,sell_price):
    ind = db.session.execute(db.select(Nifty.industry).filter_by(symbol=symbol)).scalar_one()
    npe = Portfolio(name=symbol,price=sell_price,position="Short",industry=ind)
    db.session.add(npe) 
    db.session.commit()

    return redirect(url_for('portfolio'))



