from flask import Flask, request, abort
import os
import ast

app = Flask(__name__)

app.config['SECRET_KEY'] = '0ff7d16e80eea2593e0c64b661df7cd123456789'

@app.route("/")
def home():
    return "Welcome to the safer Flask app"

@app.route("/eval")
def safer_eval():
    code = request.args.get("code")
    if not code:
        return "no code provided", 400

    try:
        result = ast.literal_eval(code)
    except (ValueError, SyntaxError):
        abort(400, "only simple literal expressions allowed")
    return str(result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)