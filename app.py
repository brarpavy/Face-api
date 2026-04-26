from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verify-identity', methods=['POST'])
def verify_identity():
    data = request.json

    # Temporary test response
    return jsonify({
        "verified": True,
        "distance": 0.2,
        "consistency": 0.1
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)