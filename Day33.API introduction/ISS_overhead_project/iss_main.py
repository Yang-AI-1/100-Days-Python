import requests
from datetime import datetime
import smtplib

MY_LAT = -1.292066 # Your latitude
MY_LONG = 36.821945 # Your longitude

def station_close_by():
    """Compares my position in long lat to the position of the ISS space station"""
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True
    return False

def is_night():
    """Checks if my current hour is beyond the sunset time and before the sunrise and returns true or false depending."""
    if sunrise >= current_hour >= sunset: #Nightime condition.Can use inequality comparisons.
        return True
    return False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
day_data = response.json()
sunrise = int(day_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(day_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

#Email info set up.
my_email = "dylantest01@gmail.com"
my_password = "gqlo cads lhjb ndrb"

if station_close_by() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="etyangdylanokomol@gmail.com",
                            msg="Subject:Stars Above.\n\nHey Dylan!Look up!The Iss station is about to be right above you ^_^")
# BONUS: run the code every 60 seconds.