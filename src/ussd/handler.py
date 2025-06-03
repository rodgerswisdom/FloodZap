import os
from flask import Flask, request


def call_rag_engine(area, emergency, people, phone_number):
    """
    Simulate a call to the RAG-based AI engine.
    Replace this with actual API call to your AI backend.
    """
    # Example output from AI engine
    return (
        f"Area: {area}\n"
        f"Emergency: {emergency}\n"
        f"Affected: {people}\n\n"
        "Move to St. Peter’s Church using the main road. It’s safe.\n"
        "Rescue ETA: 10 mins. Stay calm.\n\n"
        "- FloodZap Team"
    )


def send_ussd():
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text         = request.values.get("text", "")

    # Split user input into steps
    steps = text.split("*") if text else []

    # Step 0: Language selection
    if text == '':
        response  = "CON Welcome to FloodZap. Choose your language\n"
        response += "1. English\n"
        response += "2. Kiswahili"

    # Step 1: Area selection
    elif len(steps) == 1:
        response  = "CON Select your area\n"
        response += "1. Budalangi\n"
        response += "2. Kisumu\n"
        response += "3. Tana River\n"
        response += "4. Garissa\n"
        response += "5. Nairobi"

    # Step 2: Emergency type
    elif len(steps) == 2:
        response  = "CON What emergency are you facing?\n"
        response += "1. Flooding in my area\n"
        response += "2. I am stranded\n"
        response += "3. Someone else needs help"

    # Step 3: Who is affected
    elif len(steps) == 3:
        response  = "CON Who is affected?\n"
        response += "1. Children\n"
        response += "2. Elderly\n"
        response += "3. Pregnant Woman\n"
        response += "4. Injured Person\n"
        response += "5. Multiple people"

    # Step 4: Confirm and call AI engine
    elif len(steps) == 4:
        area_map = {
            "1": "Budalangi",
            "2": "Kisumu",
            "3": "Tana River",
            "4": "Garissa",
            "5": "Nairobi"
        }
        emergency_map = {
            "1": "Flooding in my area",
            "2": "Stranded",
            "3": "Someone else needs help"
        }
        people_map = {
            "1": "Children",
            "2": "Elderly",
            "3": "Pregnant Woman",
            "4": "Injured Person",
            "5": "Multiple people"
        }
        area = area_map.get(steps[1], "Unknown")
        emergency = emergency_map.get(steps[2], "Unknown")
        people = people_map.get(steps[3], "Unknown")

        response  = "CON Confirm report:\n"
        response += f"Area: {area}\n"
        response += f"Emergency: {emergency}\n"
        response += f"Affected: {people}\n"
        response += "\n1. Confirm\n2. Cancel"

    # Step 5: Process confirmation
    elif len(steps) == 5 and steps[4] == "1":
        area_map = {
            "1": "Budalangi",
            "2": "Kisumu",
            "3": "Tana River",
            "4": "Garissa",
            "5": "Nairobi"
        }
        emergency_map = {
            "1": "Flooding in my area",
            "2": "Stranded",
            "3": "Someone else needs help"
        }
        people_map = {
            "1": "Children",
            "2": "Elderly",
            "3": "Pregnant Woman",
            "4": "Injured Person",
            "5": "Multiple people"
        }
        area = area_map.get(steps[1], "Unknown")
        emergency = emergency_map.get(steps[2], "Unknown")
        people = people_map.get(steps[3], "Unknown")

        # Call the AI engine for stay-safe plan
        plan = call_rag_engine(area, emergency, people, phone_number)
        response = f"END Report received.\n{plan}"

    elif len(steps) == 5 and steps[4] == "2":
        response = "END Report cancelled. Stay safe!"

    else:
        response = "END Invalid choice"

    return response

