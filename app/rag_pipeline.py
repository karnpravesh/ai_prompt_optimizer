from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.redis import RedisVectorStore
from llama_index.storage.storage_context import StorageContext
import os
from config import OPENAI_API_KEY, REDIS_HOST, REDIS_PORT

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

redis_store = RedisVectorStore(index_name="prompt_optimizer", redis_host=REDIS_HOST, redis_port=REDIS_PORT)

def build_index(source_dir="data"):
    documents = SimpleDirectoryReader(source_dir).load_data()
    storage_context = StorageContext.from_defaults(vector_store=redis_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    return index

def query_index(query):
    storage_context = StorageContext.from_defaults(vector_store=redis_store)
    index = VectorStoreIndex.from_vector_store(vector_store=redis_store, storage_context=storage_context)
    return index.as_query_engine().query(query)
