from flask import Flask

app = Flask(__name__, template_folder='../templates')  # Adjust path if needed

from app import routes
