import pandas as pd
# Used to load and manipulate dataset (CSV file in this case)

from sklearn.model_selection import train_test_split
# Split dataset into training and testing parts

from sklearn.feature_extraction.text import TfidfVectorizer
# Converts text into numerical form using TF-IDF

from sklearn.linear_model import LogisticRegression
# Machine learning classification algorithm

import pickle
# Used to save trained model and vectorizer to disk

# Load dataset

data = pd.read_csv("news.csv")
# Reads dataset from csv file
# Expected columns:
# text -> news content
# label -> 0 (fake) or 1 (real)

# Split features and labels

X = data["text"]
# Input feature (news text)

y = data["label"]
# Output label (fake or real)

# Text to number conversion

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
# Converts text into numerical vectors
# stop_words="english" -> removes common words like "the", "is"
# max_features=5000 -> important words only

X_vec = vectorizer.fit_transform(X)
# Learns vocabulary + converts all text into TF-IDF matrix

# Train test split

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)
# 80% training data -> model learns from it
# 20% testing data -> used for evaluation

# Model training

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
# Saves trained ML model

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
# Saves TF-IDF vectorizer (must be reused during prediction)

# Success Message

print("Model trained successfully")
# Confirms training is complete