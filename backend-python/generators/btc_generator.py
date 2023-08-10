from bitcoinaddress import Wallet

class BtcAddrGenerator():
    def __init__(self):
        pass

    def generate(self):

        try:
            created_wallet = Wallet()
            print("wallet:", str(created_wallet.address), "key:", str(created_wallet.address))
            return {
                "result": "ok",
                "error": "",
                "data": {
                    "privkey": str(created_wallet.key),
                    "pubkey": str(created_wallet.address)
                }
            }
        except Exception as error:
            return {
                "result": "error",
                "error": error,
                "data": {
                    "privkey": "",
                    "pubkey": ""
                }
            }
                
    def create_download_link():
        pass