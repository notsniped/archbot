from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def keep_alive():
    try:
        app.run(host="0.0.0.0", port=5000)
    except OSError:
        app.run(host="0.0.0.0", port=8080)

#def keep_alive():
#    server = Thread(target=run)
#    server.start()
