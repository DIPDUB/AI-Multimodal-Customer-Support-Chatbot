import streamlit as st
from textblob import TextBlob
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDlBF7qO3uyqvnIcphuFb-YuhG-qLj-6iA"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("Sentiment Aware Chatbot")

user_input = st.text_input("Enter your message")

if user_input:

    sentiment = TextBlob(user_input).sentiment.polarity

    if sentiment > 0:
        emotion = "positive"
    elif sentiment < 0:
        emotion = "negative"
    else:
        emotion = "neutral"

    prompt = f"""
    The user message sentiment is {emotion}.
    Respond appropriately to the user.

    User message: {user_input}
    """

    response = model.generate_content(prompt)

    st.write("Sentiment detected:", emotion)
    st.write("Bot:", response.text)