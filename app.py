from flask import Flask, request, jsonify
from data_analyst_agent import ask_data_analyst

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        question = data.get("question", "")
        answer = ask_data_analyst(question)
        return jsonify({"answer": answer.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
