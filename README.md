# FRT_ENA

### FRT project

### Industry type: 
Fin Tech


### Project Title: 
Equity News Analyser


### Problem Statement:  
To analyse the effect of news on the price and volume of an equity/stock/share from NSE(National Stock                       Exchange) NIFTY-50.


### Project Description: 
  
 **Core Idea** - To Build a web tool that can analyse the effect of news on the price and volume of an equity/stock/share from     NSE(National Stock Exchange) NIFTY-50. 

  **Technologies used** - HTML, CSS, Flask, SQLite, Azure app services, Azure blob storage, Azure AI bot service.

  **Working** -  The web app collects the latest news about the stock and then depending on whether the news is good or bad the     system classifies it into Long(Good news) or Short(Bad news) category. At the time of news breakout mostly people lose       money due to late entry into the market or early exit from the market. So in order to prevent loss, now the user is          presented with Past price volume action data and current data where the user is given analysis about the effect of news      on the stock and then depending on choice of user he/she can buy or sell the stock. The portfolio displays all the           active holding of the user and its profit/loss and the portfolio diversification chart.


### Azure Services used:
   **Azure Core Services** -
   1. Azure App Services - For delpoying the Flask based web application and also deploying the azure AI Bot.
      
   3. Azure Blob Storage - For storing all the images being used in the application and then publising it to the webpage.
      
      <img width="960" alt="Storage_account" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/876335fb-e114-4b81-b999-cf3172d5592d">

      
   **Azure AI Service** -
   1. Azure AI Bot service - For creating and embedding a chat bot in the web application which can answer basic questions about the application.

      <img width="960" alt="Custom QnA" src="https://github.com/ADC-1747/FRT_ENA/assets/148060235/85a3946e-857b-4eb5-acc2-fa6b29f5fb00">

      


