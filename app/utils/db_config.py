from pymilvus import connections

def connect_to_db():
    try:
        connections.connect("default", host="localhost", port="19530")
        print("Connected to DB")
    except Exception as e:
        print(f"Can't Connect to DB {e}")
        raise
