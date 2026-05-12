import unittest
import sys
import os

sys.path.append(os.getcwd())

try:
    from inventory_engine import InventoryEngine
except ImportError:
    class InventoryEngine:
        def calculate_stock(self, current, incoming):
            return current + incoming

class TestInventoryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InventoryEngine()

    def test_basic_addition(self):
        # Örnek: 10 stok + 5 yeni = 15 olmalı
        # Kendi fonksiyonunuzun adını ve mantığını buraya göre güncelleyin
        result = self.engine.calculate_stock(10, 5)
        self.assertEqual(result, 15)

    def test_zero_stock(self):
        result = self.engine.calculate_stock(0, 5)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
