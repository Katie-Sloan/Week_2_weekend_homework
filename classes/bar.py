class Bar:
    def __init__(self):
        self.drinks = []
        self.tabs = []

    def drinks_count(self):
        return len(self.drinks)
    
    def add_drink(self, drink):
        self.drinks.append(drink)

    def serve_drink(self, drink):
        for drink in self.drinks:
            if drink.name == drink.name:
                self.drinks.remove(drink)

    def add_drink_to_tab(self, guest, drink):
        guest.tab += drink.price

    def add_entry_fee_to_tab(self, guest):
        guest.tab += 5

    def buy_drink(self, guest, drink):
        guest.wallet -= drink.price

    def pay_tab(self, guest):
        guest.wallet -= guest.tab
        guest.tab -= guest.tab
        


