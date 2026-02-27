class FlightData:
    def __init__(self,price,origin_airport,destination_airport,departure_date,return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date

    @staticmethod
    def find_cheapest_flight(flight_offer):
        """This function receives the raw JSON data from the Amadeus flight search API and parses it to be able to
        give the data."""
        try:
            price = float(flight_offer[0]["price"]["total"])
            origin_airport = flight_offer[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_airport = flight_offer[0]["itineraries"][0]["segments"][-1]["arrival"]["iataCode"] #-1 because the rest of the items in the list are stopover airports.
            departure_date = flight_offer[0]["itineraries"][0]["segments"][0]["departure"]["at"]
            return_date = flight_offer[0]["itineraries"][1]["segments"][0]["departure"]["at"]

            return FlightData(price,origin_airport,destination_airport,departure_date.split("T")[0],return_date.split("T")[0])

        except IndexError: #Only feasible error in the file.
            return FlightData(price=None,origin_airport=None,destination_airport=None,departure_date=None,return_date=None)

#TODO.REVISIONS:
# 1. Angela's code had the flight offer fetch all the flight offers as opposed to mine which returns one result.
# she does this for the sake of comparison. It is in comprehension that the first flight isn't necessarily the cheapest even if the
# api is designed to ideally return the first flight as the cheapest one. She basically creates an instance for comparison and compares
# the rest of the flight offers grand totals.
# 2. Her methods have comprehensive documentation on the parameters, overarching logic and return values (along with other notes).