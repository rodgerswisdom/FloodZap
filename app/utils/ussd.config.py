import os
import africastalking
from dotenv import laod_env

getenv = load_env

# Replace with your actual credentials
username = "sandbox"     # or live app username
api_key = os.getenv('AT_API') # get this from the dashboard

# Initialize SDK
africastalking.initialize(username, api_key)

# Example: Send SMS
ussd = africastalking.USSD

def send_sms():
    response = ussd.send("Hello from Flask!", ["+2547XXXXXXXX"])
    print(response)

