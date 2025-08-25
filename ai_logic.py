from flask import Blueprint, render_template, request, jsonify, session, redirect
import PyPDF2
import nltk
import json
import re
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Configura Gemini
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

nltk.download("punkt", quiet=True)

ai_bp = Blueprint("ai_bp", __name__)

# --- Função manual ---
def manual_classification(text):
    keywords_produtivo = ["status", "requerimento", "atualização", "dúvida", "suporte", "problema", "arquivo"]
    if any(kw in text.lower() for kw in keywords_produtivo):
        return "Produtivo", "Obrigado pelo contato. Estamos verificando sua solicitação e retornaremos em breve."
    return "Improdutivo", "Obrigado pela sua mensagem!"

# --- Função IA ---
def classify_with_ai(text):
    try:
        prompt = f"""
        Você é um assistente que classifica emails para uma empresa do setor financeiro.

        Email recebido:
        \"\"\"{text}\"\"\"

        Responda apenas em JSON no formato:
        {{
            "categoria": "Produtivo" ou "Improdutivo",
            "resposta": "texto da resposta automática"
        }}
        """
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response = model.generate_content(prompt)
        content = response.text.strip()

        # Remove ```json e ```
        content = re.sub(r"^```json", "", content, flags=re.IGNORECASE)
        content = re.sub(r"```$", "", content)

        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            result = json.loads(match.group(0))
            return result.get("categoria"), result.get("resposta")
        return None, None
    except Exception as e:
        print("Erro na IA:", e)
        return None, None

# --- Rotas ---
@ai_bp.route("/")
@ai_bp.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/login")
    return render_template("dashboard.html", username=session.get("username"))

@ai_bp.route("/process", methods=["POST"])
def process_email():
    if not session.get("logged_in"):
        return jsonify({"error": "Usuário não autenticado"}), 403

    email_text = ""
    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        if file.filename.endswith(".txt"):
            email_text = file.read().decode("utf-8")
        elif file.filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file)
            email_text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif "text" in request.form:
        email_text = request.form["text"]

    if not email_text.strip():
        return jsonify({"error": "Nenhum conteúdo de email recebido."}), 400

    categoria, resposta = classify_with_ai(email_text)
    if not categoria or not resposta:
        categoria, resposta = manual_classification(email_text)

    return jsonify({"categoria": categoria, "resposta": resposta})
