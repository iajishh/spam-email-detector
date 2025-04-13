import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

MODEL_PATH = 'spam_model.pkl'
VECTORIZER_PATH = 'vectorizer.pkl'

# Train and save only if not already saved
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    # Load dataset
    data = pd.read_csv('data/spam_dataset.csv')

    # Clean dataset
    data.dropna(subset=['text', 'label'], inplace=True)

    # Vectorize
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['text'])
    y = data['label']

    # Train model
    model = MultinomialNB()
    model.fit(X, y)

    # Save model and vectorizer
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

# Prediction function
def predict_spam(text):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    input_vec = vectorizer.transform([text])
    prediction = model.predict(input_vec)
    return 'Spam' if prediction[0] == 1 else 'Not Spam'
