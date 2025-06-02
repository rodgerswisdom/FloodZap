import os
from flask import Flask, request, jsonify
from ussd import send_ussd

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        data = {"message":"✅ server is alive!!"}
        return jsonify(data)
    return "hello SafeNow"

@app.route("/ussd", methods=['POST'])
def ussd():
    response = send_ussd()
    return response


@app.route("/dashboard")
def dashboard():
    return "People should work together"

if __name__ == "__main__":
    app.run(debug = True)

