import unittest
import sys
import os

sys.path.append(os.getcwd())
from inventory_engine import InventoryEngine

class TestInventoryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InventoryEngine()

    def test_logic(self):
        # BURAYI KENDİ KODUNUZA GÖRE DÜZENLEYİN
        # Örnek: result = self.engine.fonksiyon_adiniz(parametreler)
        # self.assertEqual(result, beklenen_deger)
        self.assertTrue(hasattr(self.engine, '__init__'))

if __name__ == "__main__":
    unittest.main()
