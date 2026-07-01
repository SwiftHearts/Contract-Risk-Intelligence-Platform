import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

search_endpoint = os.getenv("SEARCH_ENDPOINT")
search_key = os.getenv("SEARCH_KEY")
index_name = os.getenv("SEARCH_INDEX_NAME")

client = SearchClient(
    endpoint=search_endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(search_key)
)
results = client.search(
    search_text="termination clause"
)

for result in results:
    print("\n====================")
    print("Title:", result["title"])
    print("Chunk:")
    print(result["chunk"])