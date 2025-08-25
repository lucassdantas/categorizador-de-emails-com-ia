from flask import Blueprint, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os

# Configura Gemini
load_dotenv()
envLogin = os.getenv("LOGIN")
envPassword = os.getenv("PASSWORD")

login_bp = Blueprint("login_bp", __name__)

# Usuário estático
STATIC_USER = {"username": envLogin, "password": envPassword}

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == STATIC_USER["username"] and password == STATIC_USER["password"]:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("ai_bp.dashboard"))
        else:
            return render_template("login.html", error="Usuário ou senha incorretos")
    return render_template("login.html", error=None)

@login_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_bp.login"))
