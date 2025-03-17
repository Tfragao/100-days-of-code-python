import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

WEATHER_CONDITION = 700
OPENWEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")

parameters = {
    "lat" : 43.2627,
    "lon" : -2.9253,
    "appid" : api_key,
    "cnt" : 4
}

condition_codes = []
response = requests.get(url=OPENWEATHER_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    condition_codes.append(weather_id)
for weather_condition in condition_codes:
    if weather_condition < WEATHER_CONDITION:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="This is Taison here.It is going to rain today, remember to bring an umbrella ☔",
        from_="your number here ",
        to="number where you want to send",

    )
