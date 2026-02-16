import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
MY_LAT = -1.292066
MY_LNG = 36.821945

parameters ={
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json",params= parameters)
response.raise_for_status()
day_data = response.json()
sunrise = day_data["results"]["sunrise"].split("T")[1].split(":")[0] #The extra splitting is to just give us the hour time.
sunset = day_data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

print(dt.datetime.now().hour)

