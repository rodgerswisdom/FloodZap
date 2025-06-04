class WatsonXClient:
    """Client for interacting with IBM watsonx.ai API."""
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
        self.base_url = "https://api.watsonx.ai/v1/generate"

    def generate_response(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": 150
        }
        response = self._make_api_call(headers, data)
        return response

    def _make_api_call(self, headers, data):
        import requests
        try:
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json().get("generated_text", "")
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error: {http_err}"}
        except Exception as err:
            return {"error": f"General error: {err}"}

    def _handle_error(self, error):
        # Placeholder for error handling logic
        print(f"An error occurred: {error}")