import requests
import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
from twilio.rest import Client

def drop_or_rise():
    """Returns rise or fall emoji along with the percentage"""
    percentage = (close_difference / float(day_before_yesterday_close)) * 100 #Absolute percentage.
    if float(yesterday_close) > float(day_before_yesterday_close):
        return f"⬆️ {percentage:.2f}%"  # rose
    else:
        return f"⬇️ {percentage:.2f}%"  # dropped

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()

AVS_STOCK_APIKEY = os.getenv("AVS_STOCK_APIKEY")
NEWS_APIKEY = os.getenv("NEWS_APIKEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AVS_STOCK_APIKEY #Variables in string format
}
#-------------- Stocks API and close price comparisson -------------#
#TODO.This section involves obtaining stock data from the specific stock and
# finding the difference between the close price for yesterday and the day before.

response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
data = response.json()
stock_data = data["Time Series (Daily)"]
stock_data_list = [value for i,(key,value) in enumerate(stock_data.items()) if i < 2] #The list contains the data for the last 2 days.
yesterday_close = stock_data_list[0]["4. close"]
day_before_yesterday_close = stock_data_list[1]["4. close"]
close_difference = abs(float(yesterday_close) - float(day_before_yesterday_close)) #Absolute value.

#-------------------- NEWS API --------------------#
#TODO.In this section I configure the news client API and format the article to send to the user.
newsapi = NewsApiClient(api_key=NEWS_APIKEY)
top_headlines = newsapi.get_everything(q="Tesla TSLA",
                                       language="en",
                                       page_size= 3,
                                       sort_by="publishedAt"
                                          )
articles = top_headlines["articles"]
article_format = """ """
for article in articles:
    title = article.get("title") or "No title available"
    description = article.get("description") or f"{article.get('url')}"
    article_format += f"\nHeadline: {title}\nBrief: {description}\n"

final_article = f"TSLA: {drop_or_rise()} \n{article_format}"

# ---------- Twilio Client API ------------ #
#TODO.In this section I set up the condition In order to alert me of fluctuations in the TSLA stock market
# and send the message through twilio whatsapp.
percentage_change = (close_difference / float(day_before_yesterday_close)) * 100 #Absolute percentage change.
if percentage_change >= 2:
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body= final_article,
        from_="whatsapp:+14155238886",
        to="whatsapp:+254714938076"
    )
    print(message.status)
else:
    print(f"No significant movement. Change was only {percentage_change:.2f}%. No message sent.")