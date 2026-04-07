import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📄 Simple Document Q&A Chatbot")
st.markdown("Upload a TXT document and ask questions about its content. The chatbot will find the most relevant sentence as an answer.")
st.background_color = "#f0f0f0"
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload TXT file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    # Split into sentences
    sentences = text.split(".")

    df = pd.DataFrame(sentences, columns=["sentence"])

    st.success("Document uploaded successfully!")

    question = st.text_input("Ask a question:")

    if question:
        # Convert to lowercase
        question_words = question.lower().split()

        # Score sentences
        scores = []
        for sent in df["sentence"]:
            count = sum(word in sent.lower() for word in question_words)
            scores.append(count)

        df["score"] = scores

        # Get best answer
        answer = df.sort_values(by="score", ascending=False).iloc[0]["sentence"]

        st.write("### 🤖 Answer:")
        st.write(answer)