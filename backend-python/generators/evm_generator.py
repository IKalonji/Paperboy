from eth_account import Account
import secrets
import os
import uuid

class EvmAddrGenerator():
    def __init__(self):
        pass

    def generate(self):
        try:
            uuid_generated = uuid.uuid4()
            unique_download_id = str(uuid_generated)
            unpadded_key = secrets.token_hex(32)
            prefixed_key = "0x" + unpadded_key
            generate_pub_addr = Account.from_key(prefixed_key)
            result = self.writer(f"wallet: {generate_pub_addr.address}\nkey: {prefixed_key}", unique_download_id)
            print(result)
            return {
                "result": "ok",
                "error": "",
                "download": f"{unique_download_id}.txt",
                "data": {
                    "pubkey": generate_pub_addr.address,
                    "privkey": prefixed_key
                }
            }
        except Exception as error:
            return {
                "result": "error",
                "error": str(error),
                "download": "",
                "data": {
                    "pubkey": "",
                    "privkey": ""
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