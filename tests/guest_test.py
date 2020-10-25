import unittest
from classes.guest import *
from classes.room import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Nicola", 100, "Independent Women", "Coldplay")
        self.guest_2 = Guest("Boris", 4, "Bicycle Race", "Adele")
        self.room = Room("Paris", 2)

    def test_guest_has_name(self):
        self.assertEqual("Nicola", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest_1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Independent Women", self.guest_1.favourite_song)

    def test_guest_has_favourite_artist(self):
        self.assertEqual("Coldplay", self.guest_1.favourite_artist)

    def test_guest_tab_starts_at_0(self):
        self.assertEqual(0, self.guest_1.tab)

    def test_sufficient_funds__true_if_enough(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(True, self.guest_1.sufficient_funds(self.guest_1))

    def test_sufficient_funds__false_if_not_enough(self):
        self.room.check_in_guest(self.guest_2)
        self.assertEqual(False, self.guest_2.sufficient_funds(self.guest_2))

    def test_guest_can_pay_entry_fee__where_sufficient_funds(self):
        self.guest_1.pay_entry_fee(self.guest_1)
        self.assertEqual(95, self.guest_1.wallet)

    def test_guest_cannot_pay_entry_fee__where_insufficient_funds(self):
        self.guest_2.pay_entry_fee(self.guest_2)
        self.assertEqual("Sorry, you can't afford entry", self.guest_2.pay_entry_fee(self.guest_2))
    
 




   

    
    