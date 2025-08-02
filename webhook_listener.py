# webhook_listener.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def github_event():
    payload = request.json
    # Process commit info, trigger eval or logging
    print("Received GitHub Push:", payload)
    return '', 204
