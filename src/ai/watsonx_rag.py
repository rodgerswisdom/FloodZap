class WatsonXRAG:
    def __init__(self, api_key, model_name, milvus_client):
        self.api_key = api_key
        self.model_name = model_name
        self.documents = []
        self.milvus_client = milvus_client

    def load_documents(self, documents):
        self.documents = documents

    def retrieve_relevant_documents(self, user_query):
        relevant_docs = self.milvus_client.search_documents(user_query)
        return relevant_docs

    def generate_response(self, user_query):
        relevant_docs = self.retrieve_relevant_documents(user_query)
        response = self._create_response(relevant_docs)
        return response

    def _create_response(self, relevant_docs):
        if relevant_docs:
            return f"Here are the relevant documents: {', '.join(relevant_docs)}"
        else:
            return "No relevant documents found."