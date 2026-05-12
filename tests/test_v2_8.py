import unittest
import sys
import os

sys.path.append(os.getcwd())

class TestLogic8(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
