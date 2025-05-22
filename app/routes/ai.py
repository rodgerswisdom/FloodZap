from flask import Blueprint, request, jsonify
from app.services.watson_ai import WatsonAIService

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai/endpoint', methods=['POST'])
def ai_endpoint():
    data = request.json
    response = WatsonAIService.process_request(data)
    return jsonify(response), 200

@ai_bp.route('/ai/status', methods=['GET'])
def ai_status():
    status = {"status": "AI service is running"}
    return jsonify(status), 200

@ai_bp.route('/ai/evaluate', methods=['POST'])
def ai_evaluate():
    evaluation_data = request.json
    evaluation_result = WatsonAIService.evaluate_data(evaluation_data)
    return jsonify(evaluation_result), 200