from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Here you would process the user_message and generate a response
    response_message = f"You said: {user_message}"  # Placeholder response
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)