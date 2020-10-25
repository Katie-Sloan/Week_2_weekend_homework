import unittest
from classes.drink import *

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Irn Bru", 3)

    def test_drink_has_name(self):
        self.assertEqual("Irn Bru", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)