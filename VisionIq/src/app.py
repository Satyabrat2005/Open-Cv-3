import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="IQryx",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 VisionIQ")
st.subheader("Ask your video anything")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Ask a question about the video")

if st.button("Ask") and question:
    payload = {"question": question}
    response = requests.post(API_URL, json=payload).json()

    st.session_state.chat.append({
        "question": question,
        "answer": response["answer"],
        "results": response["results"]
    })

for item in st.session_state.chat[::-1]:
    st.markdown(f"### ❓ {item['question']}")
    st.markdown(f"**🧠 Answer:** {item['answer']}")

    with st.expander("📷 Visual Evidence"):
        for r in item["results"]:
            st.write(
                f"Frame: {r['frame_id']} | "
                f"Time: {r['timestamp']}s | "
                f"Objects: {', '.join(r['objects'])}"
            )
