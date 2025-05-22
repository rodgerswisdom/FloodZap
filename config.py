import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///data/safenow.db'
    WATSON_AI_API_KEY = os.environ.get('WATSON_AI_API_KEY') or 'your_watson_ai_api_key'
    RISK_ENGINE_URL = os.environ.get('RISK_ENGINE_URL') or 'http://localhost:5000/risk'
    INCIDENTS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'incidents.json')
    SHELTERS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'shelters.json')