import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Nicola", 100, "Independent Women", "Coldplay")
        self.guest_2 = Guest("Boris", 4, "Bicycle Race", "Adele")
        self.guest_3 = Guest("Donald", 20, "Wonderwall", "Oasis")
        self.room = Room("Paris", 2)
        self.song_1 = Song("Wonderwall", "Oasis")
        self.song_2 = Song("Independent Women", "Destiny's Child")
        self.song_3 = Song("Supersonic", "Oasis")

    def test_room_has_name(self):
        self.assertEqual("Paris", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_room_has_guests(self):
        self.assertEqual(0, self.room.guests_count())

    def test_room_has_playlist(self):
        self.assertEqual(0, self.room.song_count())

    def test_room_has_price(self):
        self.assertEqual(5, self.room.price)

    def test_room_can_check_in_guests(self):
        self.room.check_in_guest(self.guest_1) 
        self.assertEqual(1, self.room.guests_count())

    def test_room_can_check_out_guests(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room.guests_count())

    def test_room_can_add_songs(self):
        self.room.add_song(self.song_2)
        self.assertEqual(1, self.room.song_count())

    def test_room_cannot_check_in_guest_to_full_room(self): 
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2) 
        self.assertEqual("Sorry, room is full", self.room.check_in_guest(self.guest_3))
    
    def test_guest_favourite_song_on_playlist__True(self):
        self.room.add_song(self.song_2)
        self.room.check_in_guest(self.guest_1)
        self.assertEqual("Wooo", self.room.check_playlist(self.guest_1))

    def test_guest_favourite_song_on_playlist__False(self):
        self.room.add_song(self.song_1)
        self.room.check_in_guest(self.guest_1)
        self.assertEqual("Never mind", self.room.check_playlist(self.guest_1))

    def test_guest_favourite_artist_on_playlist(self):
        self.room.add_song(self.song_3)
        self.assertEqual("Not my favourite but still, what a tune", self.room.find_songs_by_favourite_artist(self.guest_3))
