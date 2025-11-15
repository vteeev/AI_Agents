from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    # Process the data and generate a response
    response = {"message": "Hello, World!"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')