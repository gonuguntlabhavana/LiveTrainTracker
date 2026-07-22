import requests
from datetime import datetime

API_KEY = "rg_7e19673278a34901a270dafeaef792ec"

BASE_URL = "https://api.railradar.in/v1"


def get_live_status(train_number):

    url = f"{BASE_URL}/trains/{train_number}/live"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    params = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "include": "all"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response
def get_train_details(train_number):

    url = f"{BASE_URL}/trains/{train_number}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response