from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"hello": "world"})

@app.route('/health', methods=['GET'])
def health_check():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)