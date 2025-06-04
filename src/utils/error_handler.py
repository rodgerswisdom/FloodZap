class ErrorHandler:
    """Centralized error handling for the API."""
    @staticmethod
    def handle_api_error(error):
        return {
            "error": "API Error",
            "message": str(error)
        }, 500

    @staticmethod
    def handle_milvus_error(error):
        return {
            "error": "Milvus Error",
            "message": str(error)
        }, 500

    @staticmethod
    def handle_json_error(error):
        return {
            "error": "JSON Formatting Error",
            "message": str(error)
        }, 400

    @staticmethod
    def handle_general_error(error):
        return {
            "error": "General Error",
            "message": str(error)
        }, 500

    @staticmethod
    def handle_error(error):
        return ErrorHandler.handle_general_error(error)