## Spam Email Detector Web App

This is a Flask-based web application that predicts whether a given email text is spam or not spam using a trained machine learning model.

---

## Features

- Spam Detection: Classifies email content as spam or ham (not spam).
- Machine Learning: Uses a vectorizer and trained classifier to process and analyze email content.
- Web Interface: Simple HTML-based form for testing email input.
- Packaged Model: Loads a `.pkl` file containing the trained model and vectorizer.

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- HTML/CSS (Flask templates)
- Gunicorn (for deployment)

---

## Project Structure

spam-email-detector/ ├── app/ # Application logic (optional modular folder) ├── data/ # Dataset or processed data files ├── templates/ # HTML templates for Flask ├── venv/ # Virtual environment (excluded from deployment) ├── main.py # Main Flask app ├── requirements.txt # Project dependencies ├── spam_model.pkl # Trained spam classification model ├── vectorizer.pkl # Text vectorizer used during training └── .gitattributes

yaml
Copy
Edit

---

## Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/iajishh/spam-email-detector.git
   cd spam-email-detector
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python main.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
Deployment
To deploy on platforms like Render, ensure the following:

gunicorn is listed in requirements.txt.

The web service starts with:

css
Copy
Edit
gunicorn main:app
