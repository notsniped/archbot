from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def getrnd():
    random.randint(1000,9999)
    return rnd

def run():
    try:
        app.run(host="0.0.0.0", port=6969)
    except OSError:
        app.run(host="0.0.0.0", port=getrnd())

def keep_alive():
    server = Thread(target=run)
    server.start()
