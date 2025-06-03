from flask import Blueprint, request, jsonify
from src.ai.rag_pipeline import RAGPipeline
from src.utils.logger import log_request, log_response
from src.utils.error_handler import handle_error

api_bp = Blueprint('api', __name__)

rag_pipeline = RAGPipeline()

@api_bp.route('/generate_plan', methods=['POST'])
def generate_plan():
    try:
        data = request.json
        user_query = data.get('query')
        
        if not user_query:
            return jsonify({"error": "Query is required."}), 400
        
        log_request(user_query)
        response = rag_pipeline.process_query(user_query)
        log_response(response)
        
        return jsonify({
            "success": True,
            "data": {
                "plan": response
            }
        }), 200

    except Exception as e:
        return handle_error(e)