from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    # Process the data here
    return jsonify({"message": "Data received", "data": data})

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')