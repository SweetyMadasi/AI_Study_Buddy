import streamlit as st
from transformers import pipeline

st.title("📚 AI Study Buddy")

# Create AI summarizer
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

# User input
user_text = st.text_area("Enter your topic or notes here:")

if st.button("Explain / Summarize"):
    if user_text:
        result = summarizer(user_text, max_length=100, min_length=30)
        st.subheader("AI Output:")
        st.write(result[0]['summary_text'])
    else:
        st.warning("Please enter some text first!")