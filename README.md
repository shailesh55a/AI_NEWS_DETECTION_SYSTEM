# AI News Intelligence System

A machine learning and generative AI application that analyzes news articles and provides:

- Fake News Detection
- Sentiment Analysis
- AI-Generated Summary

The goal of this project is to combine traditional machine learning techniques with modern LLM-based summarization to help users quickly understand and evaluate news content.

---

## Features

### Fake News Detection
Uses TF-IDF vectorization and Logistic Regression to classify news as Real or Fake.

### Sentiment Analysis
Analyzes article tone and classifies it as:
- Positive
- Negative
- Neutral

### AI Summary Generation
Uses Groq's LLaMA 3 model to generate concise summaries of lengthy news articles.

---

## Tech Stack

### Frontend
- Streamlit

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

## Project Structure

```text
ai-news-intelligence/
│
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
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
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd ai-news-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Training the Model

Place your dataset as:

```text
news.csv
```

Expected columns:

```text
text
label
```

Train the model:

```bash
python train_model.py
```

This will generate:

```text
model.pkl
vectorizer.pkl
```

---

## Running the Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Running with Docker

Build image:

```bash
docker build -t ai-news-intelligence .
```

Run container:

```bash
docker run -p 8501:8501 ai-news-intelligence
```

---

## Future Improvements

- BERT-based fake news detection
- Live news integration using NewsAPI
- News credibility scoring
- User authentication
- Historical analysis dashboard

---

## Author

Shailesh Bahirat

BSc Artificial Intelligence & Machine Learning