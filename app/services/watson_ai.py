from flask import jsonify, request
import requests

class WatsonAIService:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def send_request(self, data):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(self.endpoint, json=data, headers=headers)
        return response.json()

    def get_response(self, user_input):
        data = {
            'input': user_input
        }
        return self.send_request(data)