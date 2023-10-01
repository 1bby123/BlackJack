class Player: 
    def __init__(self, name):
        self.hand = []
        self.total = 0
        self.name = name
        

    def Hit(self, card):
        self.hand.append(card)

    def addHand(self):
        num_aces = 0
        self.total = 0
        for card in self.hand:
            if card.rank != "Ace":
                self.total += card.getValue()
            else:
                num_aces += 1

        while num_aces > 0:
            if self.total + 11 <= 21:
                self.total += 11
            else:
                self.total += 1
            num_aces -= 1

        return self.total
    
    def checkAce(self, card):
        if card.rank == "Ace":
            if self.total <= 21:
                card.value = 11
            elif self.total > 21:
                card.value = 1

        self.addHand()

    def checkBlackJack(self):
        if self.total == 21:
            return True

    def printHand(self):
        for card in self.hand:
            print(card.rank , "of" , card.suit)
            
        print("")

    def printCard(self, card):
        print(card.rank , "of" , card.suit)
        
    def printTotal(self):
        print("Current total:" , self.total , "")

    

    
    
class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
        
    pass 