from flask import Blueprint, request, jsonify

ussd_bp = Blueprint('ussd', __name__)

@ussd_bp.route('/ussd', methods=['POST'])
def ussd_menu():
    user_input = request.form.get('user_input')
    session_id = request.form.get('session_id')
    
    # Logic for handling USSD menu interactions
    if user_input == "1":
        response = "Welcome to the Flood Response System. Press 1 for Incident Reporting, 2 for Shelter Information."
    elif user_input == "2":
        response = "Please provide your location for shelter information."
    else:
        response = "Invalid input. Please try again."
    
    return jsonify({"response": response, "session_id": session_id})

@ussd_bp.route('/ussd/session', methods=['POST'])
def manage_session():
    session_id = request.form.get('session_id')
    action = request.form.get('action')
    
    # Logic for managing user sessions
    if action == "start":
        # Start a new session
        return jsonify({"message": "Session started", "session_id": session_id})
    elif action == "end":
        # End the session
        return jsonify({"message": "Session ended", "session_id": session_id})
    
    return jsonify({"message": "Invalid action"})