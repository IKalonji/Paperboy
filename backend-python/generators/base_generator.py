import os
from generators.networks import Networks

class Base_Generator(Networks):

    def __init__(self, network):
        self.network = network
        os.mkdir(network)
        
    def generate(self):
        '''Generate pub & priv key: to be overriden and implemented by inheriting class'''
        pass
    def create_download_link(self):
        '''Create a file link for optional key file download: to be overriden and implemented by inheriting class'''
        pass