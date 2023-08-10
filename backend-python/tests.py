import os
import unittest
from generators.btc_generator import BtcAddrGenerator
from generators.evm_generator import EvmAddrGenerator

class TestGenerators(unittest.TestCase):

    def setUp(self):
        """Create uuid_files Folder"""
        try:
            os.mkdir("uuid_files")
        except FileExistsError as error:
            print("Skipping, folder exists")

    def test_btc_generator(self):
        """Test BTC Generator"""
        generator = BtcAddrGenerator()
        result = generator.generate()
        self.assertEqual(result.get("result"), "ok", "Should be ok")
        self.assertEqual(result.get("error"), "", "Should not have an error")
        # this test is applied for github actions as the worker no longer supports openssl ripemd160 hash function
        # if result.get("error") == "unsupported hash type ripemd160":
        #     self.assertEqual(result.get("result"), "error", "Platform does not support openssl ripemd160")
        # else:
        #     self.assertEqual(result.get("result"), "ok", "Should be ok")
        #     self.assertEqual(result.get("error"), "", "Should not have an error")

    def test_evm_generator(self):
        """Test EVM Generator"""
        generator = EvmAddrGenerator()
        result = generator.generate()
        self.assertEqual(result.get("result"), "ok", "Should be ok")
        self.assertEqual(result.get("error"), "", "Should not have an error")

    def test_writer(self):
        """Test Writer"""
        generator = EvmAddrGenerator()
        result = generator.writer("hello", "hello_from_test")
        self.assertEqual(result, True, "Should be return true")
        self.assertEqual(os.path.isfile(os.path.join(os.getcwd(),"uuid_files", "hello_from_test.txt")), True, "File should be created")
        

if __name__ == '__main__':
    unittest.main()