# 🧠 AI News Intelligence System

An AI-powered application that combines **Machine Learning**, **Natural Language Processing (NLP)**, and **Generative AI** to analyze news articles. The system detects fake news, performs sentiment analysis, generates AI-powered summaries, and exposes its functionality through both a **Streamlit Web App** and a **FastAPI REST API**.

---

# 🚀 Features

- 📰 Fake News Detection  
- 😊 Sentiment Analysis  
- 🤖 AI-Generated News Summary (Groq LLM)  
- 🌐 FastAPI REST API  
- 💻 Interactive Streamlit Web Interface  
- 🐳 Docker Support  

---

# 🛠 Tech Stack

### Frontend
- Streamlit  

### Backend
- FastAPI  
- Uvicorn  

### Machine Learning
- Scikit-learn  
- TF-IDF Vectorizer  
- Logistic Regression  

### Generative AI
- Groq API (llama3-70b-8192 / llama3-8b-8192)  

### Programming Language
- Python  

---

# 📂 Project Structure

```text
AI-NEWS-INTELLIGENCE-SYSTEM/
│
├── app.py                     # Streamlit Application
├── train_model.py             # Model Training Script
├── model.pkl                  # Trained Model
├── vectorizer.pkl             # TF-IDF Vectorizer
│
├── api/
│   └── main.py                # FastAPI Backend
│
├── utils/
│   ├── preprocessing.py
│   ├── sentiment.py
│   └── summarizer.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
└── news.csv
