
import os

import requests

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = "You are ProAssist, an intelligent and motivating personal productivity assistant. Help the user organize tasks, set goals, apply productivity techniques, and stay motivated. LANGUAGE RULE: Always respond in the same language the user writes in. Use emojis in moderation. If the user shares a task, help them break it into concrete steps."

conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

@app.route("/")

def index():

    return render_template("index.html")

@app.route("/chat", methods=["POST"])

def chat():

    global conversation_history

    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:

        return jsonify({"error": "empty"}), 400

    api_key = os.environ.get("GROQ_API_KEY") or os.environ.get("proassist") or os.environ.get("PROASSIST")

    if not api_key:

        return jsonify({"response": "⚠️ Error: La variable de entorno GROQ_API_KEY no está configurada en Render."}), 200

    conversation_history.append({"role": "user", "content": user_message})

    model = os.environ.get("GROQ_MODEL", "qwen/qwen3.8-27b")

    try:

        response = requests.post(

            GROQ_URL,

            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},

            json={"model": model, "messages": conversation_history, "max_tokens": 1024},

            timeout=30

        )

        result = response.json()

    except Exception as e:

        return jsonify({"response": f"⚠️ Error de conexión al servicio de IA: {str(e)}"}), 200

    if "choices" not in result:

        err_msg = result.get("error", {}).get("message", str(result))

        return jsonify({"response": f"⚠️ Error de Groq: {err_msg}"}), 200

    assistant_message = result["choices"][0]["message"]["content"]

    conversation_history.append({"role": "assistant", "content": assistant_message})

    return jsonify({"response": assistant_message})

@app.route("/reset", methods=["POST"])

def reset():

    global conversation_history

    conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

    return jsonify({"status": "ok"})

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    app.run(host="0.0.0.0", port=port)

