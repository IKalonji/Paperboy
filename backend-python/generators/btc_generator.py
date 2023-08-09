from generators.base_generator import Base_Generator
from bitcoinlib.wallet import Wallet
from bitcoinlib.mnemonic import Mnemonic
from bitcoinaddress import Wallet

class BtcAddrGenerator(Base_Generator):
    def __init__(self):
        super().__init__(self.BTC)
    def generate(self):
        seed = Mnemonic().generate()
        w = Wallet.create("", keys=seed, network='bitcoin')
        print(w)
                
    def create_download_link():
        pass