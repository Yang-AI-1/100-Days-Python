import requests
parameters = {
    "amount":10,
    "type":"boolean"
}
response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status() #To raise an error when the call fails.
question_data = response.json()["results"]
