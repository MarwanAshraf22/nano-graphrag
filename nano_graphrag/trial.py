from dotenv import load_dotenv
from nano_graphrag import GraphRAG, QueryParam

# Load environment variables
load_dotenv()

# Initialize GraphRAG
graph_func = GraphRAG(working_dir="./dickens")

# Load and insert content from the file
with open("./book.txt", "r", encoding="utf-8") as f:
    graph_func.insert(f.read())

# Perform local graphrag search
local_result = graph_func.query("What are the top themes in this story?", param=QueryParam(mode="local"))

# Pretty print the result in a more readable format
print("\n==================== Query Result ====================")
print(local_result)
print("\n=======================================================")
