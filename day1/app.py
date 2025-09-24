from flask import Flask
import os

# hardcoded intentionally for practicing gitleaks
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
db_password = "SuperSecret123!"

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")

@app.route('/')
def hello():
    return f"Hello! Secret key is: {SECRET_KEY}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
