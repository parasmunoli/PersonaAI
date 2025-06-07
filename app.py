import streamlit as st
from bot import get_response
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash")
chat = model.start_chat(history=[])


st.set_page_config(page_title="PersonaAI", page_icon="🤖")
person = st.selectbox("Choose a person to talk to:", ["Hitesh", "Piyush"])
st.title(f"💬 Talking to {person}")

hitesh_avatar = os.path.join("assets", "hitesh.jpg")
piyush_avatar = os.path.join("assets", "piyush.jpg")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask your question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        reply = get_response(user_input, chat, person=person)

    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        avatar = hitesh_avatar if person == "Hitesh" else piyush_avatar
        with st.chat_message("assistant", avatar=avatar):
            st.markdown(msg["content"])