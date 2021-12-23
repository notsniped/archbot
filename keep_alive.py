from flask import Flask, render_template, redirect
from threading import Thread
import random

app = Flask('')

@app.route('/')
def main():
    return render_template("root.html")

@app.route('/status', methods=["GET"])
def status():
    return redirect("https://stats.uptimerobot.com/J14lqcByrn")

@app.route('/amogus', methods=["GET"])
def amogus():
    return render_template("amogus.html")

@app.route('/credits', methods=["GET"])
def about():
  return render_template("credits.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html"), 404

def getrnd():
    rnd = random.randint(1000,9999)
    if rnd == 6969:
        rnd = random.randint(1000, 9999)
    return rnd

def run():
    try:
        app.run(host="0.0.0.0", port=6969)
    except OSError:
        app.run(host="0.0.0.0", port=getrnd())

def keep_alive():
    server = Thread(target=run)
    server.start()
