# 🧠 AI News Intelligence System

An AI-powered application that combines **Machine Learning**, **Natural Language Processing (NLP)**, and **Generative AI** to analyze news articles. The system detects fake news, performs sentiment analysis, generates AI-powered summaries, and exposes its functionality through both a **Streamlit Web App** and a **FastAPI REST API**.

---

# 🚀 Features

- 📰 Fake News Detection
- 😊 Sentiment Analysis
- 🤖 AI-Generated News Summary
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
- Groq API
- LLaMA 3

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
└── news.csv                   # Dataset (Optional)
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/shailesh55a/AI-NEWS-INTELLIGENCE-SYSTEM.git
cd AI-NEWS-INTELLIGENCE-SYSTEM
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 🧠 Train the Model

Place the dataset as:

```text
news.csv
```

Required columns:

```text
text
label
```

Run:

```bash
python train_model.py
```

Generated files:

```text
model.pkl
vectorizer.pkl
```

---

# 💻 Run Streamlit App

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 🌐 Run FastAPI

```bash
uvicorn api.main:app --reload
```

API:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoint

## POST `/predict`

### Request

```json
{
  "news": "Paste your news article here..."
}
```

### Response

```json
{
  "prediction": "Real News",
  "sentiment": "Positive",
  "summary": "AI-generated summary..."
}
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t ai-news-intelligence-system .
```

## Run Container

```bash
docker run -p 8501:8501 ai-news-intelligence-system
```

Open:

```
http://localhost:8501
```

---

# 🔮 Future Improvements

- BERT-based Fake News Detection
- Live News API Integration
- News Credibility Score
- User Authentication
- News History Dashboard
- Multilingual News Analysis

---

# 👨‍💻 Author

**Shailesh Bahirat**

BSc Artificial Intelligence & Machine Learning

GitHub: https://github.com/shailesh55a
