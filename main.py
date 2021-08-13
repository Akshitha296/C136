from flask import Flask, jsonify
app = Flask(__name__)
from data import data

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()