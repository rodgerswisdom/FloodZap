class RAGPipeline:
    """Retrieval-Augmented Generation pipeline for rescue plans."""
    def __init__(self, milvus_client, watsonx_client):
        self.milvus_client = milvus_client
        self.watsonx_client = watsonx_client

    def embed_query(self, user_query: str):
        """Embed the user query using the WatsonX client."""
        embedded_query = self.watsonx_client.embed(user_query)
        return embedded_query

    def search_documents(self, embedded_query):
        """Search for relevant documents in Milvus."""
        search_results = self.milvus_client.search(embedded_query)
        return search_results

    def format_prompt(self, search_results):
        """Format the prompt for watsonx.ai."""
        prompt = "Based on the following documents, please generate a rescue plan:\n"
        for result in search_results:
            prompt += f"- {result}\n"
        return prompt

    def generate_rescue_plan(self, user_query: str):
        """Generate a rescue plan using RAG."""
        try:
            embedded_query = self.embed_query(user_query)
            search_results = self.search_documents(embedded_query)
            prompt = self.format_prompt(search_results)
            response = self.watsonx_client.generate_response(prompt)
            return response
        except Exception as e:
            # Handle errors appropriately
            return {"error": str(e)}