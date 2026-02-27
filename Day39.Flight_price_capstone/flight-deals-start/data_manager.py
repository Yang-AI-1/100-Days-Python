import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = "https://api.sheety.co/14265f4b1a5633aa13008e0f1d433657/flightDeals/prices"
        self.headers = {
            "Content-Type": "application/json"
        }
    def read_sheet(self):
        """This function sends a get request and reads the data from the sheet."""
        response = requests.get(url=self.url,headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data

    def update_google_sheet(self,updated_sheet_data):
        """This function uses a sheety api put request to edit the google sheet."""
        for row in updated_sheet_data["prices"]:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.url}/{row['id']}",
                json=new_data,
                headers=self.headers
            )
            response.raise_for_status()
            print(response.text)

#TODO.REVISIONS:
# 1.I simply did not use sheety basic authentication.She did, but I just didn't want to.