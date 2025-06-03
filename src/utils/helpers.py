def validate_phone_number(phone_number):
    # Validate the phone number format (e.g., Kenyan phone numbers)
    if len(phone_number) == 10 and phone_number.isdigit():
        return True
    return False

def format_alert_message(alert):
    # Format the alert message for better readability
    return f"Alert: {alert['title']}\nDetails: {alert['details']}\nLocation: {alert['location']}"

def extract_coordinates(location):
    # Extract latitude and longitude from a location string
    # This is a placeholder function; actual implementation may vary
    return {"latitude": None, "longitude": None}  # Replace with actual extraction logic

def log_event(event):
    # Log events for monitoring and debugging
    with open('event_log.txt', 'a') as log_file:
        log_file.write(f"{event}\n")