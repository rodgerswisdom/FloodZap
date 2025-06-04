from flask import Blueprint, render_template

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@dashboard_blueprint.route('/dashboard/data')
def dashboard_data():
    # TODO: Implement dashboard data logic
    return {"message": "Dashboard data will be implemented here."}