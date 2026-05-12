import unittest
from reference.inventory_engine import InventoryEngine

class TestInventoryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InventoryEngine()

    def test_all_cases(self):
        cases = [
            (10, 2, 5, 5, 5, "Normal"),
            (2, 2, 5, 10, 18, "High"),
            (50, 1, 5, 5, 0, "Normal"),
            (10, 0, 5, 5, 0, "Normal"),
            (0, 5, 2, 10, 20, "High"),
            (5, 1, 5, 5, 5, "Normal"),
            (10, -5, 5, 5, 0, "Normal"),
            (10, 10, 1, 5, 5, "Normal"),
            (5, 0.5, 20, 5, 10, "Normal"),
            (1000, 100, 10, 500, 500, "Normal")
        ]
        for stock, vel, lead, safety, expected_qty, expected_prio in cases:
            res = self.engine.calculate_recommendation(stock, vel, lead, safety)
            self.assertEqual(res["recommendation"], expected_qty)
            self.assertEqual(res["priority"], expected_prio)

if __name__ == '__main__':
    unittest.main()
