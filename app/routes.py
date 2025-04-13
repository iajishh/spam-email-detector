from flask import render_template, request
from app import app
from app.model import predict_spam
from app.preprocess import preprocess_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email']
    processed_text = preprocess_text(email_text)
    prediction = predict_spam(processed_text)
    return render_template('result.html', prediction=prediction, email=email_text)
