import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

API_KEY= os.getenv("API_KEY")
APP_ID= os.getenv("APP_ID")
MY_NAME=os.getenv("MY_NAME")
MY_EMAIL=os.getenv("MY_EMAIL")

workout_api_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = "https://api.sheety.co/14265f4b1a5633aa13008e0f1d433657/myWorkouts/sheet1"

workout_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
workout_data_input = {
    "query":input("Describe the completed exercise.Mention the activity, duration/distance:\n")
}
#-------API request for workout API info-----------#
response = requests.post(url=workout_api_endpoint, headers=workout_headers, json=workout_data_input)
response.raise_for_status()
data = response.json()
exercise = data["exercises"][0]["name"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

#-----Current Date time-------#
now = datetime.now()
date_formatted = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

#----Sheety API put requests--------#
sheety_headers = {
    "Content-Type": "application/json"
}
body = {
    "sheet1": {
        "date": date_formatted,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
response = requests.post(url=sheety_endpoint,json=body,headers=sheety_headers)
response.raise_for_status()
