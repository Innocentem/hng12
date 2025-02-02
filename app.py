from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "mwbzinno@gmail.com",
        "current_datetime": datetime.utcnow().isoformat(timespec='seconds') + "Z",  # Corrected
        "github_url": "https://github.com/Innocentem/hng12.git"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
