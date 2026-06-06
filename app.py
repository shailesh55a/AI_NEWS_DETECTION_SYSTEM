import streamlit as st
# Streamlit is used to build the web interface

import pickle
# Pickle is used to load saved ML models

from utils.preprocessing import clean_text
from utils.sentiment import analyze_sentiment
from utils.summarizer import summarize_news

# Load trained model and vectorizer

# Load the trained logistic Regression model
# This model was created in train_model.py
model = pickle.load(open("model.pkl","rb"))

# Load the TF-IDF vectorizer
# Important: must be the same vectorizer used during traning
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Streamlit page configuration

# Configure browser tab title and layout
st.set_page_config(
    page_title="AI News Intelligence System",
    layout="wide"
)

# Application title
st.title("🧠 AI News Intelligence System")

st.write(
    """
This application can:
    ✅ Detect Fake News
    
    ✅ Analyze Sentiment
    
    ✅ Generate AI Summary using Groq LLM
    """
)

# User input section

# Multi-line text box where user enters news article
news = st.text_area(
    "Paste News Article Here",
    height=250
)
 
# Anlayze button

# Execute analysis only when button is clicked
if st.button("Analyze News"):

    # Check if user entered any text
    if not news.strip():
        
        st.warning("Please enter a news article.")

    else:
        
        # Preprocess text

        # Clean text before ML prediction
        cleaned_text = clean_text(news)

        # Convert text to TF-IDF vector

        # transform user into numerical features
        news_vector = vectorizer.transform([cleaned_text])

        # Fake news prediction

        prediction = model.predict(news_vector)[0]

        # Display result
        st.subheader("📰 Fake News Detection")

        if prediction == 1:

            st.success("Real News ✅")

        else:

            st.error("Fake News ❌")

        # Sentiment analysis

        sentiment = analyze_sentiment(cleaned_text)

        st.subheader("😊 Sentiment Analysis")

        st.info(sentiment)

        # AI summary generation

        st.subheader("🤖 AI Generated Summary")

        # Show loading spinner while waiting doe LLM response
        with st.spinner("Generating summary..."):
            
            summary = summarize_news(news)
        
        st.write(summary)
