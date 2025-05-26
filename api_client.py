import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def get_jwt():
    print('Fetching JWT...')
    if not API_URL:
        raise ValueError("API_URL must be set in the environment variables.")
    
    response = requests.post(f'{API_URL}/auth', json={"email": EMAIL, "password": PASSWORD})
    
    if response.status_code == 401:
        raise ValueError("Invalid credentials. Please check your email and password.")
    elif response.status_code != 200:
        raise ValueError(f"Failed to fetch JWT: {response.status_code} - {response.text}")

    return response.json().get("token")

def get_sales():
    print('Fetching sales data...')
    token = get_jwt()  
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f'{API_URL}/sales', headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(f"API_URL from env: {API_URL}")

    sales_data = get_sales()
    print(sales_data)
