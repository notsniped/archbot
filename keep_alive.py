from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    try:
        app.run(host="0.0.0.0", port=6969)
    except OSError:
        app.run(host="0.0.0.0", port=4200)

def keep_alive():
    server = Thread(target=run)
    server.start()
