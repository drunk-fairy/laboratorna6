import random

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def info_rank(self):
        return self.rank

    def __str__(self):
        
