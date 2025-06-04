from flask import Blueprint, request, jsonify
from src.ai.rag_pipeline import RAGPipeline
from src.ai.milvus_client import MilvusClient
from src.ai.watsonx_client import WatsonXClient
from src.utils.logger import app_logger
from src.utils.error_handler import ErrorHandler

api_bp = Blueprint('api', __name__)

# Instantiate clients (use dummy values for now)
milvus_client = MilvusClient()
watsonx_client = WatsonXClient(api_key="dummy", model_name="dummy")
rag_pipeline = RAGPipeline(milvus_client, watsonx_client)

def log_request(data):
    app_logger.info(f"Request: {data}")

def log_response(data):
    app_logger.info(f"Response: {data}")

def handle_error(e):
    app_logger.error(f"Error: {e}")
    return ErrorHandler.handle_general_error(e)

@api_bp.route('/generate_plan', methods=['POST'])
def generate_plan():
    try:
        data = request.json
        user_query = data.get('query')
        if not user_query:
            return jsonify({"error": "Query is required."}), 400
        log_request(user_query)
        response = rag_pipeline.generate_rescue_plan(user_query)
        log_response(response)
        return jsonify({
            "success": True,
            "data": {
                "plan": response
            }
        }), 200
    except Exception as e:
        return handle_error(e)