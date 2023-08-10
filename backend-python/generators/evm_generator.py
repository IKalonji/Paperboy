from eth_account import Account
import secrets

class EvmAddrGenerator():
    def __init__(self):
        pass

    def generate(self):
        try:
            unpadded_key = secrets.token_hex(32)
            prefixed_key = "0x" + unpadded_key
            generate_pub_addr = Account.from_key(prefixed_key)
            print("wallet:", generate_pub_addr.address, "key:", prefixed_key)
            return {
                "result": "ok",
                "error": "",
                "data": {
                    "pubkey": generate_pub_addr.address,
                    "privkey": prefixed_key
                }
            }
        except Exception as error:
            return {
                "result": "error",
                "error": error,
                "data": {
                    "pubkey": "",
                    "privkey": ""
                }
            }

    def create_download_link():
        pass