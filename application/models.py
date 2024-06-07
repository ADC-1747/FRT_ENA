from .database import db

class Nifty(db.Model):
    __tablename__ = 'nifty'
    n_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String)
    company_name = db.Column(db.String)
    industry = db.Column(db.String)

class LNews(db.Model):
    __tablename__ = 'lnews'
    l_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ln = db.Column(db.String)
    ls = db.Column(db.String)


class SNews(db.Model):
    __tablename__ = 'snews'
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sn = db.Column(db.String)
    ss = db.Column(db.String)

class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    industry = db.Column(db.String)
    price = db.Column(db.Float)

    