import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/14265f4b1a5633aa13008e0f1d433657/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/14265f4b1a5633aa13008e0f1d433657/flightDeals/users"
class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)

    def get_customer_emails(self):
        """Returns data from the users sheet in the Flight-Deals google sheet.
        Makes a get request from sheety and returns all the data un the users sheet in json format."""
        print("Obtaining customer Data")
        response = requests.get(url=SHEETY_USERS_ENDPOINT,auth=self._authorization)
        response.raise_for_status()
        print("Customer Data successfully retrieved")
        return response.json()["users"]