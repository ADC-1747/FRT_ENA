# FRT_ENA

### FRT project

### Industry type: 
Fin Tech


### Project Title: 
Equity News Analyser


### Problem Statement:  
To analyse the effect of news on the price and volume of an equity/stock/share from NSE(National Stock Exchange) NIFTY-50.


### Project Description: 
  
 **Core Idea** - To Build a web tool that can analyse the effect of news on the price and volume of an equity/stock/share from NSE(National Stock Exchange) NIFTY-50. 

  **Technologies used** - HTML, CSS, Flask, SQLite, Azure app services, Azure blob storage, Azure AI bot service.

  **Working** -  The web app collects the latest news about the stock and then depending on whether the news is good or bad the system classifies it into Long(Good news) or Short(Bad news) category. At the time of news breakout mostly people lose money due to late entry into the market or early exit from the market. So in order to prevent loss, now the user is presented with Past price volume action data and current data where the user is given analysis about the effect of news on the stock and then depending on choice of user he/she can buy or sell the stock. The portfolio displays all the active holding of the user and its profit/loss and the portfolio diversification chart.


### Azure Services used:
   **Azure Core Services** -
   1. Azure App Services - For delpoying the Flask based web application and also deploying the azure AI Bot.

      <img width="960" alt="web_app" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/443847d7-1e95-4889-8a23-6d4026f250f5">


      <img width="960" alt="Deploy" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/feedc98b-02ef-47c2-825a-c8b0fbb81bf6">


      
   2. Azure Blob Storage - For storing all the images being used in the application and then publising it to the webpage.
      
      <img width="960" alt="Storage_account" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/876335fb-e114-4b81-b999-cf3172d5592d">

      
   **Azure AI Service** -
   1. Azure AI Bot service - For creating and embedding a chat bot in the web application which can answer basic questions about the application.

      <img width="960" alt="app_bot" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/a41fefd0-b1c1-4007-a206-9f9108d8aac6">


      <img width="960" alt="Custom QnA" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/85a3946e-857b-4eb5-acc2-fa6b29f5fb00">

      <img width="960" alt="rg1" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/42380a6c-0633-45fe-8cb0-84d0ee6a30bf">

      <img width="960" alt="rg2" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/eb100a00-4008-4ddb-bfe1-7b5ed987e2ea">




### Interconnectivity between Services:
The Azure App Service and the Azure AI Bot service are interconnected as the app services host the bot so that it can be used in the application.
The Azure Blob storage is interconnected with the Azure App Services as the images stored in the Azure Blob storage are used in the application and hosted on the web.
All the Azure services used are interconnected and thier interconnectivity is essential for the functionality of the project.


<img width="960" alt="app_home" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/8d411be7-eee7-4c8c-8872-9663282394ae">

<img width="959" alt="app_news" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/20e20c67-48d2-458f-b057-7524ac016175">

<img width="960" alt="app_bot" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/11dd54a5-eb2f-43c5-82ba-77de5698f683">

<img width="960" alt="app_analyse" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/9d5dbfb5-4920-422c-8b43-c2e7abdaebbf">

<img width="960" alt="app_port_1" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/29b4f390-636f-488c-9bfc-0801f3d80841">

<img width="960" alt="app_port_2" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/bb63ca9f-dee8-437e-8822-c99966b112b2">


### Note:- Upon clicking any of the refresh news or news or portfolio or update portfolio or analyse or buy or sell buttons please wait for around 30 to 40 seconds as it takes time to search and load the real time market data. For best user experience use when the Indian Trading Market is open.




      


