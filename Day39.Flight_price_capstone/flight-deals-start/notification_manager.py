from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    def send_message(self,flight_data):
        message = self.client.messages.create(
            body=f'''Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_airport} to {flight_data.destination_airport}
            from {flight_data.departure_date} to {flight_data.return_date}''',
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=f"whatsapp:{MY_PHONE_NUMBER}"
        )
        print(message.status)


