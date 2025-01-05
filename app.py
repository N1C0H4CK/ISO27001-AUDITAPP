from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example data
controls = {
    "Operations HRO": [
        {"number": "A.5.1.1", "description": "Policies for Information Security", "owner": "John Doe", "lastReview": "2025-01-01", "signOff": "Pending", "evidence": ""},
    ],
    "Operations SDM": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Application Management Solutions": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Global Technology": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Service Readiness": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Products & Offering": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Sales & Pre-Sales": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Finance": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Office Management": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Local IT": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Legal": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Training Team": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Health & Safety": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Recruitment": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],
    "Compliance": [
        {"number": "A.6.1.4", "description": "Separation of Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""},
    ],

}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/api/getControls', methods=['GET'])
def get_controls():
    team = request.args.get('team')
    return jsonify(controls.get(team, []))

if __name__ == '__main__':
    app.run(debug=True)
