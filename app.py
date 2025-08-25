from flask import Flask, request, jsonify, render_template
import os
import PyPDF2
import nltk
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai  # lib do Gemini

# pip install flask PyPDF2 nltk google-generativeai

# configure a chave do Gemini no ambiente
#genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("Chave Gemini carregada:", bool(api_key))

nltk.download("punkt", quiet=True)

app = Flask(__name__)

# --- Função de fallback manual ---
def manual_classification(text):
    """Classificação simples baseada em palavras-chave"""
    keywords_produtivo = ["status", "requerimento", "atualização", "dúvida", "suporte", "problema", "arquivo"]
    if any(kw in text.lower() for kw in keywords_produtivo):
        return "Produtivo", "Obrigado pelo contato. Estamos verificando sua solicitação e retornaremos em breve."
    return "Improdutivo", "Obrigado pela sua mensagem!"

# --- Função que tenta usar a IA (Gemini) ---
def classify_with_ai(text):
    try:
        prompt = f"""
        Você é um assistente que classifica emails para uma empresa do setor financeiro.

        Email recebido:
        \"\"\"{text}\"\"\"

        Responda **apenas** em JSON no formato:
        {{
            "categoria": "Produtivo" ou "Improdutivo",
            "resposta": "texto da resposta automática"
        }}
        """

        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response = model.generate_content(prompt)

        content = response.text.strip()
        print("DEBUG raw content:", repr(content))

        # --- Remove ```json e ``` se existir ---
        content = re.sub(r"^```json", "", content, flags=re.IGNORECASE)
        content = re.sub(r"```$", "", content)

        # --- Extrai apenas o JSON do texto ---
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            json_str = match.group(0)
            result = json.loads(json_str)
            return result.get("categoria"), result.get("resposta")
        else:
            print("Nenhum JSON encontrado na resposta da IA.")
            return None, None

    except Exception as e:
        print("Erro na IA:", e)
        return None, None

# --- Rotas ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_email():
    email_text = ""

    # --- Arquivo enviado ---
    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        if file.filename.endswith(".txt"):
            email_text = file.read().decode("utf-8")
        elif file.filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file)
            email_text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())

    # --- Texto enviado diretamente ---
    elif "text" in request.form:
        email_text = request.form["text"]

    if not email_text.strip():
        return jsonify({"error": "Nenhum conteúdo de email recebido."}), 400

    # --- Tenta IA primeiro ---
    categoria, resposta = classify_with_ai(email_text)

    # --- Se IA falhar, usa manual ---
    if not categoria or not resposta:
        categoria, resposta = manual_classification(email_text)

    return jsonify({"categoria": categoria, "resposta": resposta})



if __name__ == "__main__":
    app.run(debug=True)
