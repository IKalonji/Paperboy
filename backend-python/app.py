from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")

@app.route("eth-create", methods=["GET"])
def generateEvmAddr():
    return {"result": "ok", "addr": "addressHere", "priv": "privKeyHere"}

@app.route("btc-create", methods=["GET"])
def generateBtcAddr():
    return {"result": "ok", "addr": "addressHere", "priv": "privKeyHere"}

if __name__=="__main__":
    app.run(port=5555, host="0.0.0.0")
