import os
import unittest
from generators.btc_generator import BtcAddrGenerator
from generators.evm_generator import EvmAddrGenerator

class TestGenerators(unittest.TestCase):

    def test_btc_generator(self):
        generator = BtcAddrGenerator()
        result = generator.generate()
        self.assertEqual(result.get("result"), "ok", "Should be ok")
        self.assertEqual(result.get("error"), "", "Should not have an error")

    def test_evm_generator(self):
        generator = EvmAddrGenerator()
        result = generator.generate()
        self.assertEqual(result.get("result"), "ok", "Should be ok")
        self.assertEqual(result.get("error"), "", "Should not have an error")

    def test_writer(self):
        generator = EvmAddrGenerator()
        try:
            os.mkdir("uuid_files")
        except FileExistsError as error:
            print("Skipping, folder exists")
        result = generator.writer("hello", "hello_from_test")
        self.assertEqual(result, True, "Should be return true")
        self.assertEqual(os.path.isfile(os.path.join(os.getcwd(),"uuid_files", "hello_from_test.txt")), True, "File should be created")
        try:
            os.rmdir("uuid_files")
        except Exception as error:
            print("Could not delete folder")

if __name__ == '__main__':
    unittest.main()