
from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def study_assistant(question, mode="tutor"):
    if mode == "tutor":
        system_prompt = "You are a helpful AI tutor. Explain simply with examples."
    elif mode == "exam":
        system_prompt = "Give short exam-ready answers."
    else:
        system_prompt = "Summarize content in bullet points."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
