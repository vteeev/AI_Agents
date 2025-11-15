from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/job-application', methods=['POST'])
def job_application():
    data = request.json
    # Process the job application data here
    # For example, save to a database or send an email
    return jsonify({"message": "Job application received", "data": data}), 201

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')