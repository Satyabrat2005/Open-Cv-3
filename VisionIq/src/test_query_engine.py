from query_engine import QueryEngine

engine = QueryEngine(top_k=5, use_llm=True)

while True:
    q = input("\n💡 IQryx Query (type 'exit' to quit)\n> ")
    if q.lower() == "exit":
        break

    response = engine.query(q)

    print("\nANSWER")
    print("-" * 50)
    print(response["answer"])

    print("\n📷 MATCHED FRAMES")
    print("-" * 50)
    for r in response["results"]:
        print(
            f"Rank {r['rank']} | "
            f"Score: {r['score']:.3f} | "
            f"Frame: {r['frame_id']} | "
            f"Objects: {', '.join(r['objects'])}"
        )
