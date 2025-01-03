from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data
controls = {
    "HR": [
        {"number": "A.5.1.1", "description": "Policies for Information Security", "owner": "John Doe", "lastReview": "2025-01-01", "signOff": "Pending", "evidence": ""},
        {"number": "A.7.2.2", "description": "Screening", "owner": "Jane Smith", "lastReview": "2024-12-15", "signOff": "Signed Off", "evidence": "/path/to/evidence.pdf"}
    ],
    "IT": [
        {"number": "A.6.1.4", "description": "Separation of Development, Test, and Production Environments", "owner": "Alice Brown", "lastReview": "2024-11-20", "signOff": "Pending", "evidence": ""}
    ]
}

@app.route('/api/getControls', methods=['GET'])
def get_controls():
    team = request.args.get('team')
    return jsonify(controls.get(team, []))

if __name__ == '__main__':
    app.run(debug=True)
