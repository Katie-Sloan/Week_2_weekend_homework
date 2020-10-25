class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.songs = []
        self.price = 5

    def guests_count(self):
        return len(self.guests)
    
    def check_in_guest(self, name):
        if self.capacity == len(self.guests):
            return("Sorry, room is full")
        else: 
            self.guests.append(name)

    def check_out_guest(self, name):
        for guest in self.guests:
            if guest == name:
                self.guests.remove(name)

    def song_count(self):
        return len(self.songs)
    
    def add_song(self, name):
        self.songs.append(name)

    def check_playlist(self, guest):
        for song in self.songs:
            if song.name == guest.favourite_song:
                return("Wooo")
            else:
                return("Never mind")

    def find_songs_by_favourite_artist(self, guest):
        for song in self.songs:
            if song.artist == guest.favourite_artist and song.name != guest.favourite_song:
                return("Not my favourite but still, what a tune")

        
        

    