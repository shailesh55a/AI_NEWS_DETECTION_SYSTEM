from fastapi import FastAPI
from pydantic import BaseModel
import pickle

from utils.preprocessing import clean_text
from utils.sentiment import analyze_sentiment
from utils.summarizer import summarize_news

# load trained model and vectorizer
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# create Fastapi app

app = FastAPI(
    title="AI News Intelligence System API",
    description="API for Fake News Detection, Sentiment Analysis and AI summary" ,
    version="1.0"
)

# input schema

class NewsRequest(BaseModel):
    news: str

# home endpoint
@app.get("/")
def home():
    return {"message": "AI News Intelligence System API is running."}

# prediction endpoint
@app.post("/predict")
def predict(request: NewsRequest):

    # clean input text
    cleaned_text = clean_text(request.news)

    # convert to TF-IDF vector
    news_vector = vectorizer.transform([cleaned_text])

    # predict
    prediction = model.predict(news_vector)[0]
    result = "Real News" if prediction == 1 else "Fake News"

    # sentiment
    sentiment = analyze_sentiment(cleaned_text)

    # AI summary 
    summary = summarize_news(request.news)

    return {
        "prediction": result,
        "sentiment": sentiment,
        "summary": summary
    }
