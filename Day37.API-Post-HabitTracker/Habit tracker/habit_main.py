import requests
from datetime import datetime

TOKEN ="AlQo92IeKdNc83"
USERNAME = "okomol"
GRAPH_ID = "graph1"

#------------User creation------------#
pixela_endpoint = "https://pixe.la/v1/users" #/v1/users Is for post requests.
user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params) #Endpoint and JSON data we want to send over.
# print(response.text)

#--------------Graph creation---------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Music Practice Graph",
    "unit": "minute",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#--------------- Pixel Creation ----------------#
now = datetime.now()
formated_date = now.strftime("%Y%m%d")

pixel_addition_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": formated_date,
    "quantity": "60.0"
}
# response = requests.post(pixel_addition_endpoint,json=pixel_config,headers=headers)
# print(response.text)

#----------------- Pixel updating(existing data) ----------------#
pixel_update_endpt = f"{pixel_addition_endpoint}/{formated_date}"
pixel_update_config = {
    "quantity": "42.3"
}
# response = requests.put(url=pixel_update_endpt,json=pixel_update_config,headers=headers)
# print(response.text)

#------------------- Pixl Deletion --------------------#
pixel_delete = f"{pixel_addition_endpoint}/{formated_date}"

response = requests.delete(url=pixel_delete,headers=headers)
print(response.text)