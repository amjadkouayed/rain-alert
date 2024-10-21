import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

API = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")

twilio_number = os.getenv("twilio_number")
recieving_number = os.getenv("recieving_number")



parameters = {

    "lat": 53.349804,
    "lon": -6.260310,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get(API, params= parameters)
response.raise_for_status()
data = response.json()

is_raining = False

for weather in data["list"]:
    
    if int(weather["weather"][0]["id"]) < 700:
        is_raining = True
 


if is_raining:
    account_sid = os.getenv("account_sid")
    auth_token = os.environ.get('twilio_auth_key')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=twilio_number,
    to=recieving_number,
    body="it's gonna rain today, bring an umbrella"
    )

    print(message.sid)
    
