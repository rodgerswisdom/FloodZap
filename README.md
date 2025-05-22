# My Flask App

This project is a Flask application designed to manage flood incident reports and shelter information. It includes functionalities for USSD interactions, a stakeholder dashboard, and AI integration using watsonx.ai.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py             # Flask app factory
│   ├── routes/                 # API and view routes
│   │   ├── __init__.py
│   │   ├── ussd.py             # USSD menu logic
│   │   ├── dashboard.py        # Stakeholder dashboard endpoints
│   │   └── ai.py               # AI (watsonx.ai / RAG) logic
│   │
│   ├── services/               # External service integrations
│   │   ├── __init__.py
│   │   ├── watson_ai.py        # watsonx.ai request handler
│   │   └── risk_engine.py      # Logic for risk assessment & prioritization
│   │
│   ├── models/                 # Data schemas or SQLite models
│   │   ├── __init__.py
│   │   ├── incident.py         # Flood incident reports
│   │   ├── shelters.py         # Shelter locations/status
│   │   └── users.py            # Community and stakeholder users
│   │
│   ├── static/                 # Static assets (optional for dashboard UI)
│   └── templates/              # HTML templates (if using Flask frontend)
│
├── data/                       # Mock JSON and/or SQLite DBs
│   ├── incidents.json
│   ├── shelters.json
│   └── safenow.db              # SQLite file (used in parallel)
│
├── tests/                      # Unit and integration tests
│   └── test_ussd.py
│
├── config.py                   # Configuration variables (envs, keys)
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku deployment entry
├── run.py                      # App entry point
└── README.md                   # Project overview
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python run.py
   ```

## Usage

- Access the USSD menu through the designated endpoint.
- View the stakeholder dashboard for incident and shelter information.
- Utilize AI functionalities for enhanced decision-making.

## Testing

To run the tests, use the following command:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.