
import streamlit as st
from ai import study_assistant

st.set_page_config(page_title="AI Study Assistant", layout="wide")

st.title("🎓 AI Study Assistant")

mode = st.sidebar.selectbox("Choose Mode", ["tutor", "exam", "summary"])

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask your question:")

if st.button("Ask AI"):
    if user_input:
        reply = study_assistant(user_input, mode)
        st.session_state.chat.append((user_input, reply))

for q, a in st.session_state.chat:
    st.markdown(f"### 🧑‍🎓 You: {q}")
    st.markdown(f"### 🤖 AI: {a}")
    st.divider()
