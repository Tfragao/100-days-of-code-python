import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("API_ID")
api_key = os.getenv("API_KEY")
nutrition_endpoint = os.getenv("NUTRITIONIX_API_ENDPOINT")
sheety_endpoint = os.getenv("SHEETY_API_ENDPOINT")
username = os.getenv("U_NAME")
password = os.getenv("PASSWORD")

GENDER = "male"
WEIGHT_KG = 70.5
HEIGHT_CM = 170
AGE = 25

exercise_text = input("Tell me which exercise you did:")

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

r = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
result = r.json()

################################################# Using sheety##################################
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs,
                                   auth=(username, password))
    print(sheet_response.text)