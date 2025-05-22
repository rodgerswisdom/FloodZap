from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    reported_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Incident {self.id}: {self.description}>' 

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'location': self.location,
            'severity': self.severity,
            'reported_at': self.reported_at.isoformat()
        }