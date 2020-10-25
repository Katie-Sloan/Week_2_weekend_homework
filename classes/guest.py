class Guest:
    def __init__(self, name, wallet, favourite_song, favourite_artist):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.favourite_artist = favourite_artist
        self.tab = 0

    def sufficient_funds(self, guest):
        return self.wallet >= 5

    def pay_entry_fee(self, guest):
        if self.wallet >= 5:
            self.wallet -= 5
        else:
            return("Sorry, you can't afford entry")
        


        

