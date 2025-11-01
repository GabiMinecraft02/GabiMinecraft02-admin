from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "gabiminecraft02_secret_key"  # clé pour flash messages

# 🔐 Mot de passe admin
ADMIN_PASSWORD = "latte62860."

# 📁 Dossier de stockage des uploads
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -----------------------------
# ROUTE LOGIN
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == ADMIN_PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            flash("❌ Mot de passe incorrect.")
    return render_template("login.html")

# -----------------------------
# ROUTE DASHBOARD
# -----------------------------
@app.route("/dashboard")
def dashboard():
    # Liste des images
    images = [f for f in os.listdir(UPLOAD_FOLDER)
              if f.lower().endswith((".jpg", ".png", ".jpeg", ".gif"))]

    # Lire le texte
    texts = []
    text_file = os.path.join(UPLOAD_FOLDER, "text.txt")
    if os.path.exists(text_file):
        with open(text_file, "r", encoding="utf-8") as f:
            texts = f.readlines()

    return render_template("dashboard.html", images=images, texts=texts)

# -----------------------------
# ROUTE UPLOAD IMAGE
# -----------------------------
@app.route("/upload_image", methods=["POST"])
def upload_image():
    file = request.files.get("file")
    name = request.form.get("name")
    if file and file.filename:
        filename = f"{name}_{file.filename}" if name else file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        flash(f"✅ Image '{filename}' téléchargée !")
    else:
        flash("⚠️ Aucun fichier sélectionné.")
    return redirect(url_for("dashboard"))

# -----------------------------
# ROUTE UPLOAD TEXTE
# -----------------------------
@app.route("/upload_text", methods=["POST"])
def upload_text():
    text = request.form.get("text")
    if text.strip():
        with open(os.path.join(UPLOAD_FOLDER, "text.txt"), "a", encoding="utf-8") as f:
            f.write(text + "\n\n")
        flash("✅ Texte ajouté !")
    else:
        flash("⚠️ Aucun texte saisi.")
    return redirect(url_for("dashboard"))

# -----------------------------
# LANCEMENT DE L'APPLICATION
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # port différent du site principal
