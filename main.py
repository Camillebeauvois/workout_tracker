import os
import requests
import datetime

DATE = datetime.date.today().strftime("%d/%m/%Y")
TIME = datetime.datetime.now().strftime("%H:%M:%S")

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
sheety_endpoint = os.environ["sheety_endpoint"]
nutrix_endpoint = os.environ["nutrix_endpoint"]


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("How much exercise did you do today? : "),
    "gender": "female",
    "weight_kg": 57,
    "height_cm": 179,
    "age": 34
}

response = requests.post(url=nutrix_endpoint, json=params, headers=header)
nlp_output = response.json()


for record in nlp_output["exercises"]:

    params = {
        "workout": {
            'date': DATE,
            'time': TIME,
            'exercise': record["name"],
            'duration': record["duration_min"],
            'calories': record["nf_calories"]
        }
    }

    sheety_post = requests.post(url=sheety_endpoint, json=params)
