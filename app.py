from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API Running"

@app.route('/verify-identity', methods=['POST'])
def verify_identity():
    return jsonify({
        "verified": True,
        "distance": 0.25,
        "consistency": 0.12
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
