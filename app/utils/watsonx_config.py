from ibm_watsonx_ai.foundation_models import ModelInference

def query_ibm_watson_llm(prompt: str) -> str:


    model = ModelInference(
        project_id = "0ea49f8c-3c84-4304-9aae-88a52d19e579",
        model_id="ibm/granite-3-8b-instruct",  # or another supported model
        credentials={
            "apikey": "API_KEY",
            "url": "https://us-south.ml.cloud.ibm.com"
            }
    )


    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']
