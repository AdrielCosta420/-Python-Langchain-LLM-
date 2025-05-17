import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
JWT = os.getenv("JWT")

def get_sales():
    headers = {
        "Authorization": f"Bearer {JWT}"
    }

    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()
    return response.json()