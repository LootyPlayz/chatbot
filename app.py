from flask import Flask, request, jsonify, render_template
from chatbot import get_response
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True) or {}
    user_input = data.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please type something."}), 400
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    # Render provides its own PORT env variable, fallback to 5000 for local dev
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" allows external access (needed for Render)
    app.run(host="0.0.0.0", port=port, debug=True)
