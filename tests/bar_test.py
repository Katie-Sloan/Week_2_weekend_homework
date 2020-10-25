import unittest
from classes.bar import *
from classes.drink import *
from classes.guest import *

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar()
        self.drink = Drink("Irn Bru", 3)
        self.guest_1 = Guest("Nicola", 100, "Independent Women", "Coldplay")

    def test_stock_starts_at_0(self):
        self.assertEqual(0, self.bar.drinks_count())
    
    def test_bar_can_add_drinks(self):
        self.bar.add_drink(self.drink)
        self.assertEqual(1, self.bar.drinks_count())

    def test_bar_can_serve_drinks(self):
        self.bar.add_drink(self.drink)
        self.bar.serve_drink(self.drink)
        self.assertEqual(0, self.bar.drinks_count())

    def test_bar_can_add_drink_to_tab(self):
        self.bar.add_drink_to_tab(self.guest_1, self.drink)
        self.assertEqual(3, self.guest_1.tab)

    def test_bar_can_add_entry_fee_to_tab(self):
        self.bar.add_entry_fee_to_tab(self.guest_1)
        self.assertEqual(5, self.guest_1.tab)

    def test_guest_can_buy_drink(self):
        self.bar.add_drink(self.drink)
        self.bar.serve_drink(self.drink)
        self.bar.buy_drink(self.guest_1, self.drink)
        self.assertEqual(97, self.guest_1.wallet)

    def test_guest_can_pay_tab(self):
        self.bar.add_drink(self.drink)
        self.bar.serve_drink(self.drink)
        self.bar.add_drink_to_tab(self.guest_1, self.drink)
        self.bar.add_entry_fee_to_tab(self.guest_1)
        self.bar.pay_tab(self.guest_1)
        self.assertEqual(92, self.guest_1.wallet)

    def test_tab_has_been_paid(self):
        self.bar.add_drink(self.drink)
        self.bar.serve_drink(self.drink)
        self.bar.add_drink_to_tab(self.guest_1, self.drink)
        self.bar.add_entry_fee_to_tab(self.guest_1)
        self.bar.pay_tab(self.guest_1)
        self.assertEqual(0, self.guest_1.tab)

    

    
        