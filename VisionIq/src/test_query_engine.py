from query_engine import QueryEngine

engine = QueryEngine(top_k=5, use_llm=True)

while True:
    q = input("\n💡 IQryx Query (type 'exit' to quit)\n> ")
    if q.lower() == "exit":
        break
