from flask import Flask
from login import login_bp
from ai_logic import ai_bp

app = Flask(__name__)
app.secret_key = "super_secret_key"  # para sessões

# Registra blueprints
app.register_blueprint(login_bp)
app.register_blueprint(ai_bp)

if __name__ == "__main__":
    app.run(debug=True)
