import os
from flask import Flask, render_template, redirect

# --- Port et host dès le début ---
PORT = int(os.environ.get("PORT", 5000))
HOST = "0.0.0.0"

app = Flask(__name__)

# --- Routes principales ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/backup")
def backup():
    return render_template("backup.html")

@app.route("/advancements")
def advancements():
    # redirige vers ton site Advancements
    return redirect("https://ton-domaine-advancements.onrender.com")  # change avec ton vrai URL

@app.route("/youtube")
def youtube():
    return redirect("https://www.youtube.com/@GabiMinecraft02ps3")

@app.route("/tiktok")
def tiktok():
    return redirect("https://www.tiktok.com/@gabiminecraft028?is_from_webapp=1&sender_device=pc")

@app.route("/snapchat")
def snapchat():
    return redirect("http://snapchat.com/t/sS6oPOiV")

@app.route("/discord_backup")
def discord_backup():
    return redirect("https://discord.gg/ex8Jgrm255")

@app.route("/discord_yt")
def discord_yt():
    return redirect("https://discord.gg/dZUEhNZWWD")

@app.route("/discord_snap")
def discord_snap():
    return redirect("https://snapchat.com/t/NuFx4joB")

@app.route("/minecraft_modding")
def minecraft_modding():
    return redirect("https://minecraft-ps3-moding-website.onrender.com/")

# --- Lancer le serveur ---
if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
