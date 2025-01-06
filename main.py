from flask import Flask, request, jsonify
from groq import Groq
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-70b-8192",
        )

        response_message = chat_completion.choices[0].message.content

        return jsonify({"response": response_message}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)