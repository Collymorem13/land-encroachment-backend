from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- allows frontend access

@app.route('/')
def home():
    return "Backend is running for Land Encroachment Monitoring"

@app.route('/api/encroachment', methods=['GET'])
def encroachment():
    return jsonify({
        "id": 1,
        "location": "Lupane, Zimbabwe",
        "status": "Detected",
        "area_hectares": 15.6
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
