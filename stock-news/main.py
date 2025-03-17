import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#API_KEY_STOCK = os.environ.get("API_KEY_STOCK")
API_KEY_STOCK = "your api key here"
NEWS_API_KEY = "your api key here"
TWILIO_SID = "your sid here"
TWILIO_AUTH_TOKEN = "your auth token here"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : API_KEY_STOCK
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
r = requests.get(STOCK_ENDPOINT, params=stock_parameters)
r.raise_for_status()
stock_data = r.json()
print(stock_data)

#Get yesterday's closing stock price.
data = stock_data["Time Series (Daily)"]
daily_prices = [value for (key,value) in data.items()]
yesterday_prices = daily_prices[0]
yesterday_closing_prices = yesterday_prices["4. close"]

#Get the day before yesterday's closing stock price
day_before_yesterday_prices = daily_prices[1]
day_before_yesterday_closing_prices = day_before_yesterday_prices["4. close"]

price_dif = round(abs(float(yesterday_closing_prices) - float(day_before_yesterday_closing_prices)))
print(f"Price diff {price_dif}")
up_down = None
if price_dif > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (price_dif /float(yesterday_closing_prices)) * 100
print(diff_percent)

if abs(diff_percent) > 1:  #Sometiems it needs to be adjusted manually as the difference can be lower than 5
    news_parameters = {
        "apiKey" : NEWS_API_KEY,
        "q" : COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    formatted_articles = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
                           f"Headline: {article['title']}.\n"
                           f"Brief: {article['description']}") for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        client.messages.create(
            body=article,
            from_="your number here",
            to="where you want to send"
        )



