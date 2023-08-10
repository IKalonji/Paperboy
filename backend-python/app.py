from flask import Flask
from flask import render_template
from flask_cors import CORS
from generators.btc_generator import BtcAddrGenerator
from generators.evm_generator import EvmAddrGenerator

app = Flask(__name__)
CORS(app)
evm_addr = EvmAddrGenerator()
btc_addr = BtcAddrGenerator()



@app.route("/")
def root():
    return render_template("index.html")

@app.route("/eth-create", methods=["GET"])
def generateEvmAddr():
    return evm_addr.generate()

@app.route("/btc-create", methods=["GET"])
def generateBtcAddr():
    return btc_addr.generate()

if __name__=="__main__":
    app.run(port=5555, host="0.0.0.0")
