from bitcoinaddress import Wallet
import uuid
import os

class BtcAddrGenerator():
    def __init__(self):
        pass

    def generate(self):
        try:
            uuid_generated = uuid.uuid4()
            unique_download_id = str(uuid_generated)
            created_wallet = Wallet()
            result = self.writer(f"{created_wallet.key}\n{created_wallet.address}", unique_download_id)
            print(result)
            return {
                "result": "ok",
                "error": "",
                "download": f"{unique_download_id}.txt",
                "data": {
                    "privkey": str(created_wallet.key),
                    "pubkey": str(created_wallet.address)
                }
            }
        except Exception as error:
            return {
                "result": "error",
                "error": str(error),
                "download": "",
                "data": {
                    "privkey": "",
                    "pubkey": ""
                }
            }
    def writer(self, data, unique_id):
        try:
            path = os.path.join(os.getcwd(), "uuid_files", f"{unique_id}.txt")
            file = open(path, "a+")
            file.write(data)
            file.close()
            return True
        except Exception as error:
            print(error)
            return False

# demo time