from random import randint

class Die():
    """a class of dice"""

    def __init__(self, num_sides=6):
        """default dice is D6"""
        self.num_sides = num_sides

    def roll(self):
        """return a random int between 1--sides"""
        return randint(1,self.num_sides)


