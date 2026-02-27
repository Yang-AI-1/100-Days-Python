from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.read_sheet()
notification_manager = NotificationManager()

#Incase I need to update the sheet data.
# updated_sheet_data  = flight_search.update_sheet_data(sheet_data)
# data_manager.update_google_sheet(updated_sheet_data)

#------- Flight offers -----#
for row in sheet_data["prices"]:
    print(f"Checking flights for {row['city']}")
    flight_offer = flight_search.check_flights(row["iataCode"])
    flight_data = FlightData.find_cheapest_flight(flight_offer)

    if flight_data.price is not None and flight_data.price < row["lowestPrice"] :
        notification_manager.send_message(flight_data)
    else:
        print(f"No Cheap flights found for {row['city']}")