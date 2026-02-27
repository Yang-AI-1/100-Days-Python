from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import requests

load_dotenv()
MY_IATA = "NBO"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATACODE_ENDPOINT= "https://test.api.amadeus.com/v1/reference-data/locations/cities"
OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.__api_key = os.getenv("AMADEUS_APIKEY")
        self.__api_secret= os.getenv("AMADEUS_APISECRET")
        token = self._get_new_token()
        self.headers = {
            "Authorization": f"Bearer {token}"
        }
    def update_sheet_data(self,sheet_data):
        """Uses flight searcher API to get the country Iata codes and edit the sheet data.
        edit the local sheet data here and update it from the manager class.
        Implementation:"""
        for row in sheet_data["prices"]:
            response = requests.get(url=IATACODE_ENDPOINT,headers=self.headers,params={"keyword":row["city"]})
            response.raise_for_status()
            country_data = response.json()
            iata_code = country_data["data"][0]["iataCode"]
            row["iataCode"] = iata_code
        return sheet_data

    def _get_new_token(self):
        """Request a new token from AMADEUS using my API Key, sending a post request."""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.__api_key,
            "client_secret": self.__api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT,headers=headers,data=body)
        response.raise_for_status()
        print(f"This is your access token: {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]

    def check_flights(self,destination_city_code):
        """This function makes a get request from the offers endpoint and returns raw JSON data
        containing all the flight information."""
        today = datetime.now()
        departure  = today + timedelta(days=2)
        return_date = today + timedelta(days=16)
        params = {
            "originLocationCode": MY_IATA,
            "destinationLocationCode": destination_city_code,
            "departureDate": departure.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "GBP",
            "max": 1
        }
        response = requests.get(url=OFFERS_ENDPOINT,headers=self.headers,params=params)
        response.raise_for_status()
        return response.json()["data"]

#TODO.Revisions:
# 1.Once again Angela's code has proper documentation which explains all methods comprehensively.
# 2.Her response statements are more elegant so that the developer can know the stages of success at runtime.
#  e.g: print(f"Status code {response.statuscode}. Airport IATA{response.text}) Lets the user know the get request to fetch the Iata code was successful.
# 3.She has more deliberate error handling for the IATA code retrieval. My code assumes that every country has an airport IATA.
# She also handles the error in the check_flights method incase the status code is not successful. The response prints
# the response code, informs the dev that there was a problem with the flight search and recommends checking the documentation.
# also prints the response.text to see the response body comprehensively. My runtime is absolutely Blind