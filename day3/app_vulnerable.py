from flask import Flask, request
import os

app = Flask(__name__)

# Hardcoded secret
API_KEY = "123456789-secret"

@app.route("/")
def home():
    return "Welcome to the insecure Flask app"

@app.route("/eval")
def insecure_eval():
    code = request.args.get("code")
    return str(eval(code))  # INSECURE: eval injection risk

if __name__ == "__main__":
    app.run(debug=True)
