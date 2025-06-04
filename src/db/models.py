from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    is_vulnerable = db.Column(db.Boolean, default=False)

class FloodAlert(db.Model):
    """Flood alert model."""
    id = db.Column(db.Integer, primary_key=True)
    alert_level = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Shelter(db.Model):
    """Shelter model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

class EmergencyResponse(db.Model):
    """Emergency response model."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flood_alert_id = db.Column(db.Integer, db.ForeignKey('flood_alert.id'), nullable=False)
    response_plan = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# NOTE: Use Flask-Migrate or Alembic for migrations.