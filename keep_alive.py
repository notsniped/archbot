from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
async def main():
    return render_template("root.html")

@app.route('/status', methods=["GET"])
def status():
    return "Your bot is alive!"

@app.route('/amogus', methods=["GET"])
def amogus():
    return render_template("amogus.html")

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
