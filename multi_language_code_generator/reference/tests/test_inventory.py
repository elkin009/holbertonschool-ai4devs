import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inventory_engine import InventoryEngine

class TestInventoryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InventoryEngine()

    def test_logic(self):
        cases = [
            (10, 2, 5, 5, 5), (2, 2, 5, 10, 18), (50, 1, 5, 5, 0),
            (10, 0, 5, 5, 0), (0, 5, 2, 10, 20), (5, 1, 5, 5, 5),
            (10, -5, 5, 5, 0), (10, 10, 1, 5, 5), (5, 0.5, 20, 5, 10),
            (1000, 100, 10, 500, 500)
        ]
        for stock, vel, lead, safety, expected in cases:
            res = self.engine.calculate_recommendation(stock, vel, lead, safety)
            self.assertEqual(res["recommendation"], expected)

if __name__ == '__main__':
    unittest.main()
