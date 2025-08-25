# app.py
from flask import Flask, request, jsonify, render_template
from chatbot import get_response

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
    app.run(debug=True)

    import os

    PORT = int(os.environ.get("PORT", 4000))
    app.run(host="0.0.0.0", port=PORT)

