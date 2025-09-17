from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, Land Encroachment Backend is working!"

# Example API: return encroachment data
@app.route('/api/encroachment', methods=['GET'])
def get_encroachment():
    # Example static data (later we connect to Earth Engine or DB)
    data = {
        "id": 1,
        "location": "Lupane, Zimbabwe",
        "status": "Detected",
        "area_hectares": 15.6
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
