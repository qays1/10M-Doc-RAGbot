from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():

    return "Jordan Labor Law RAG is running on Azure"