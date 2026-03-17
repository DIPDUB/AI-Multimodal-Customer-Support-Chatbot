import streamlit as st
from langdetect import detect
import google.generativeai as genai

genai.configure(api_key="YOUR API KEY")

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("Multilingual AI Chatbot")

user_input = st.text_input("Enter your message")

if user_input:

    language = detect(user_input)

    prompt = f"""
    The user language is {language}.
    Respond in the same language as the user.

    User message: {user_input}
    """

    response = model.generate_content(prompt)

    st.write("Detected language:", language)
    st.write("Bot:", response.text)
