# For this challenge I am NOT expecting your code to do anything when it runs.
# Instead your final submission will just be a series of classes that are never instantiated.
# I want to see that you can think about objects and what parameters are necessary to use them in code.


# The goal is to create a class for every object that would be necessary to build a game of MONOPOLY
# If you have not played Monopoly (the board game) feel free to ask me or just google it

# I'll start you with one example. Please note that I do not need to you to define the logic in each method
# but it would be nice if you at least give method names like I have in the example

class Player:
    def __init__(self, _token):
        self.money = 1500
        self.token = _token
        self.properties_owned = {}
        self.current_location = "GO"
        self.get_out_of_jail_cards_owned = 0

    def pay_money(self):
        pass  # Notice I am not defining the logic of what these methods do. You do not need to either.
        # The keyword "pass" just means it will not do anyting yet

    def get_money(self):
        pass

    def buy_property(self):
        pass

    def mortgage_property(self):
        pass

    def pay_mortgage_on_property(self):
        pass

    def roll_dice(self):
        pass

