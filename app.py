from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# --- Dossier pour stocker les uploads ---
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Routes ---
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    # Liste des images
    images = [f for f in os.listdir(UPLOAD_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]

    # Lire le fichier texte
    texts = []
    text_file = os.path.join(UPLOAD_FOLDER, "text.txt")
    if os.path.exists(text_file):
        with open(text_file, "r", encoding="utf-8") as f:
            texts = f.readlines()

    return render_template("dashboard.html", images=images, texts=texts)

@app.route("/upload_image", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if file and file.filename != "":
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect(url_for("dashboard"))

@app.route("/upload_text", methods=["POST"])
def upload_text():
    text_content = request.form.get("text_content", "").strip()
    if text_content:
        with open(os.path.join(UPLOAD_FOLDER, "text.txt"), "a", encoding="utf-8") as f:
            f.write(text_content + "\n")
    return redirect(url_for("dashboard"))

# --- Lancer le serveur ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
