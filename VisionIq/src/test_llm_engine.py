from llm_engine import LLMEngine

engine = LLMEngine(model="deepseek-r1")

evidence = [
  {
        "frame_id": "frame_00004.jpg",
        "timestamp": 3.2,
        "objects": ["bottle", "table"]
    },
    {
        "frame_id": "frame_00007.jpg",
        "timestamp": 5.8,
        "objects": ["laptop", "backpack"]
    }
]

query = "When does the laptop appear?"

answer = engine.generate_answer(query, evidence)

print("\nANSWER")
print("-" * 40)
print(answer)
