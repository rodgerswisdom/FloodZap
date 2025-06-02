# create_collections.py

from pymilvus import CollectionSchema, FieldSchema, DataType, Collection, list_collections
from app.utils.db_config import connect_to_db

# Connect to Milvus
connect_to_db()

# 1. Define schema for FloodZap knowledge base
embedding_field = FieldSchema(
    name="embedding",
    dtype=DataType.FLOAT_VECTOR,
    dim=768,
    description="Embedding vector of text content"
)

id_field = FieldSchema(
    name="id",
    dtype=DataType.VARCHAR,
    is_primary=True,
    auto_id=False,
    max_length=64
)

source_type_field = FieldSchema(
    name="source_type",
    dtype=DataType.VARCHAR,
    max_length=32,
    description="Type of source: bulletin, shelter, incident, sop"
)

location_field = FieldSchema(
    name="location",
    dtype=DataType.VARCHAR,
    max_length=64,
    description="Geographical tag for location"
)

raw_text_field = FieldSchema(
    name="raw_text",
    dtype=DataType.VARCHAR,
    max_length=2048,
    description="Original chunked content text"
)

# Combine into a schema
floodzap_schema = CollectionSchema(
    fields=[id_field, embedding_field, source_type_field, location_field, raw_text_field],
    description="Knowledge base for FloodZap RAG retrieval"
)

# Create the collection
collection_name = "floodzap_knowledge_base"
if collection_name not in list_collections():
    Collection(name=collection_name, schema=floodzap_schema)
    print(f"Collection '{collection_name}' created successfully.")
else:
    print(f"Collection '{collection_name}' already exists.")

