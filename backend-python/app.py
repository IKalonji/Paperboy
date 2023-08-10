from flask import Flask, send_from_directory
from flask import render_template
from flask_cors import CORS
from generators.btc_generator import BtcAddrGenerator
from generators.evm_generator import EvmAddrGenerator
import os

app = Flask(__name__)
CORS(app)
evm_addr = EvmAddrGenerator()
btc_addr = BtcAddrGenerator()

try:
    os.mkdir("uuid_files")
except FileExistsError as error:
    print("Skipping, folder exists.")

file_not_found = open(os.path.join(os.getcwd(), "uuid_files", "file_not_found.txt"), "a+")
file_not_found.write("Not found")
file_not_found.close()

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/eth-create", methods=["GET"])
def generateEvmAddr():
    return evm_addr.generate()

@app.route("/btc-create", methods=["GET"])
def generateBtcAddr():
    return btc_addr.generate()

@app.route("/download/<file_name>", methods=['GET'])
def downloadKey(file_name):
    path = os.path.join(app.root_path, 'uuid_files')
    try:
        return send_from_directory(path, file_name)
    except FileNotFoundError as error:
        return send_from_directory(path, "file_not_found.txt")

if __name__=="__main__":
    app.run(port=5555, host="0.0.0.0")
