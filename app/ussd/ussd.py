import os
from flask import Flask, request


def send_ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text         = request.values.get("text", "default")

  if text      == '':
      # This is the first request. Note how we start the response with CON
      response  = "CON Welcom to FloodZap. Choose your language \n"
      response += "1. English \n"
      response += "2. Kiswahili"

  elif text    == '1':
      # Business logic for first level response
      response  = "CON Select your area \n"
      response += "1. Budalangi \n"
      response += "2. Kisumu \n"
      response += "3. Tana River \n"
      response += "4. Garissa \n"
      response += "5. Nairobi"

  elif text   == '2':
      # This is a terminal request. Note how we start the response with END
      response = "END Your phone number is " + phone_number

  elif text  == '1*1':
      # This is a second level response where the user selected 1 in the first instance
      response = "CON What emergency you are facing? \n"
      response += "1. Flooding in my area \n"
      response += "2. I am stranded \n"
      response += "3. Someone else needs help"
      # This is a terminal request. Note how we start the response with END
     # response       = "END Your account number is " + accountNumber
  elif text == '1*1*1' or text == '1*1*2' or text == '1*1*3':
      response = "CON Who is affected? \n"
      response += "1. Children \n"
      response += "2. Elderly \n"
      response += "3. Pregnant Woman \n"
      response += "4. Injured Person \n"
      response += "5. Multiple people"
  elif text == '1*1*2*3':
      response = "CON Confirm report \n"
      response += "Area: Budalangi \n"
      response += "Emergency: Stranded \n"
      response += "People: Pregnant Woman \n"
      response += "\n 1. Confirm"
      response += "\n 2. Cancel"

  elif text == '1*1*2*3*1':
      response = "END Report received. \n" 
      response += "Move  to St. Peter’s Church using the main road. It’s safe.\n"
      response += "Rescue ETA: 10 mins. Stay calm.\n\n"
      response += "- FloodZap Team"
  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response

