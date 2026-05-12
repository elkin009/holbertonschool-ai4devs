import unittest
from reference.inventory_engine import InventoryEngine

class TestInventoryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InventoryEngine()

    def test_cases(self):
        # 1. Normal Case
        self.assertEqual(self.engine.calculate_recommendation(10, 2, 5, 5), {"recommendation": 5, "priority": "Normal"})
        # 2. Low Stock Case (High Priority)
        self.assertEqual(self.engine.calculate_recommendation(2, 2, 5, 10), {"recommendation": 18, "priority": "High"})
        # 3. Overstock Case
        self.assertEqual(self.engine.calculate_recommendation(50, 1, 5, 5), {"recommendation": 0, "priority": "Normal"})
        # 4. Zero Sales Velocity
        self.assertEqual(self.engine.calculate_recommendation(10, 0, 5, 5), {"recommendation": 0, "priority": "Normal"})
        # 5. Critical Depletion (Zero Stock)
        self.assertEqual(self.engine.calculate_recommendation(0, 5, 2, 10), {"recommendation": 20, "priority": "High"})
        # 6. Safety Stock exactly equals current stock
        self.assertEqual(self.engine.calculate_recommendation(5, 1, 5, 5), {"recommendation": 5, "priority": "Normal"})
        # 7. Negative sales velocity handling
        self.assertEqual(self.engine.calculate_recommendation(10, -5, 5, 5), {"recommendation": 0, "priority": "Normal"})
        # 8. High sales, short lead time
        self.assertEqual(self.engine.calculate_recommendation(10, 10, 1, 5), {"recommendation": 5, "priority": "Normal"})
        # 9. Low sales, very long lead time
        self.assertEqual(self.engine.calculate_recommendation(5, 0.5, 20, 5), {"recommendation": 10, "priority": "Normal"})
        # 10. Large numbers handling
        self.assertEqual(self.engine.calculate_recommendation(1000, 100, 10, 500), {"recommendation": 500, "priority": "Normal"})

if __name__ == '__main__':
    unittest.main()
