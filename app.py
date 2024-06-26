# app.py

# Import necessary modules
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Create a route that returns a JSON message
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"hello": "world"})

# Create a health check route
@app.route('/health', methods=['GET'])
def health_check():
    return '', 200

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)