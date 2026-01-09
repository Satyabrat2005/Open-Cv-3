from query_engine import QueryEngine

engine = QueryEngine(top_k=5)

while True:
    print("\n🧠 VisionIQ Query (type 'exit' to quit)")
    question = input(">> ")

    if question.lower() in ["exit", "quit"]:
        break

    response = engine.query(question)

    print("\n💡 ANSWER")
    print("-" * 40)
    print(response["answer"])

    print("\n📸 MATCHED FRAMES")
    print("-" * 40)
    for r in response["results"]:
        print(
            f"Rank {r['rank']} | "
            f"Score: {r['score']:.3f} | "
            f"Frame: {r['frame_id']}"
        )
