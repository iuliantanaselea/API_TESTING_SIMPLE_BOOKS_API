import random

import requests

URL = "https://simple-books-api.glitch.me"

#helping method for orders API
def get_token():
    random_number_1 = random.randint(1, 999999) # generates a random number between 1 and 999999
    random_number_2 = random.randint(1, 999999) # generates a random number between 1 and 999999

    data = {
        "clientName": "Iulian",
        "clientEmail": f"iulian{random_number_1}{random_number_2}@example.com"
    }
    response = requests.post(f"{URL}/api-clients", json=data)
    return response.json()['accessToken']

def create_user(clientName, clientEmail):
    data = {
        "clientName": clientName,
        "clientEmail": clientEmail
    }
    response = requests.post(f"{URL}/api-clients", json=data)
    return response

# print(get_token())
