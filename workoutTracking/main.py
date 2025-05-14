from dotenv import load_dotenv
import requests
from datetime import datetime
import os

load_dotenv()


NL_data = input("Which excercises did you do today? ")

# Request headers
headers = {
    "x-app-id": os.getenv("N_APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "Content-Type": "application/json"
}

# User profile (optional but recommended for accurate results)
user_params = {
    "query": NL_data,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 185,
    "age": 22
}

response = requests.post(
    "https://trackapi.nutritionix.com/v2/natural/exercise",
    headers=headers,
    json=user_params
)

res_data = response.json()

today = datetime.now()
date =  today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")


for exercise in res_data["exercises"]:
    row = dict()

    row["Date"] = date
    row["Time"] = time
    row["Exercise"] = exercise["name"]
    row["Duration"] = exercise["duration_min"]
    row["Calories"] = exercise["nf_calories"]


    payload = {"workout": row} 
    response = requests.post(url=os.getenv("SHEETY_POST_ENDPOINT"), json=payload)
    
    if response.status_code in [200, 201]:
        print(f"✅ Added row: {row}")
    else:
        print(f"❌ Failed to add row: {row}")
        print(response.text)