import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="VisionIQ",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 VisionIQ")
st.subheader("Ask your video anything")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Ask a question about the video")
