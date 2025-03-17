import requests
from datetime import datetime

USERNAME = "your username here"
TOKEN = "your token here"
GRAPH_ID = "your graph id here"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

#r = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#r = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
today = datetime.now()
pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "17.5",
}

quantity_to_update = {
    "quantity": "8.5"
}
#r = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
#r = requests.put(url=f"{PIXEL_ENDPOINT}/20250312", json=quantity_to_update, headers=headers)
r = requests.delete(url=f"{PIXEL_ENDPOINT}/20250312",headers=headers)




