from flask import Flask
from src.ussd.handler import ussd_blueprint
from src.dashboard.routes import dashboard_blueprint
from src.db.models import db

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config.from_envvar('APP_CONFIG')

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(ussd_blueprint, url_prefix='/ussd')
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    @app.route("/ussd", methods=["POST"])
    def ussd():
        return send_ussd()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)