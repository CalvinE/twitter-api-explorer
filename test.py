import unittest
import api as api

class TestTwitterAPI(unittest.TestCase):
    def test_1(self):
        self.assertFalse(False, False)

    def test_config(self):
        config = api.readConfig()
        self.assertIsNotNone(config)
        base_url = config["twitter_api"]["base_url"]
        self.assertIsNotNone(base_url)

if __name__ == "__main__":
    unittest.main(verbosity=5)
