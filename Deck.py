import random

#makes a card object
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = 0
        self.cardValues = {
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
        }

    

    def getValue(self):
        return self.cardValues.get(self.rank)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            self.newDeck()
            return self.cards.pop()
        
    def printCard(self, card):
        print(card.rank , "of" , card.suit)

    def shuffle(self):
        random.shuffle(self.cards)


    def newDeck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))