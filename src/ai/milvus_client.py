class MilvusClient:
    def __init__(self, host='localhost', port='19530'):
        from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
        self.host = host
        self.port = port
        self.collection_name = 'flood_documents'
        self.collection = None
        self._connect()

    def _connect(self):
        connections.connect(host=self.host, port=self.port)
        self._create_collection()

    def _create_collection(self):
        if not self._collection_exists():
            fields = [
                FieldSchema(name='id', dtype=DataType.INT64, is_primary=True, auto_id=True),
                FieldSchema(name='content', dtype=DataType.STRING),
                FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, dim=768)  # Adjust dimension as needed
            ]
            schema = CollectionSchema(fields=fields, description="Collection for flood response documents")
            self.collection = Collection(name=self.collection_name, schema=schema)

    def _collection_exists(self):
        from pymilvus import utility
        return utility.has_collection(self.collection_name)

    def insert_documents(self, documents, embeddings):
        if self.collection is not None:
            entities = [
                [i for i in range(len(documents))],  # IDs
                documents,  # Content
                embeddings  # Embeddings
            ]
            self.collection.insert(entities)

    def search_documents(self, query_embedding, top_k=5):
        if self.collection is not None:
            search_params = {"metric_type": "IP", "params": {"nprobe": 10}}
            results = self.collection.search(query_embedding, "embedding", search_params, limit=top_k)
            return results

    def disconnect(self):
        from pymilvus import connections
        connections.disconnect()