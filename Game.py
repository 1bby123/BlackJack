from Deck import *
from Player import *
import time

class Game:
    def __init__(self, players):
        self.players = players
        self.dealer = Dealer()
        self.dealerBust = False
        self.deck = Deck()
        self.winners = []
        self.round = 1

    def handOutCards(self):
        for player in self.players:
            player.Hit( self.deck.draw())
            player.Hit(self.deck.draw())
        
        self.dealer.Hit(self.deck.draw())
        self.dealer.Hit(self.deck.draw())

    def newGame(self):
        print("Game starting...")
        time.sleep(1)
        self.round = 1
        print("First round")
        time.sleep(1)
        self.newRound()
        self.playRound()

    def newRound(self):
        self.deck.shuffle()
        self.clearHands()
        self.handOutCards()

    def clearHands(self):
        self.dealer.hand = []
        for player in self.players:
            player.hand = []
        
    def playTurn(self, player):
        time.sleep(1)
        print(player.name + ", it's your turn!")
        player.addHand()
        print("Your hand:")
        player.printHand()
        player.printTotal()
        
        while True:
                if player.checkBlackJack():
                    self.winners.append(player) 
                    print("Blackjack!")
                    self.players.remove(player)
                    break
                elif player.total > 21:
                    print("Bust!")
                    self.players.remove(player)
                    break
                
                answer = input("Hit or stand?: ").lower()
                if answer == "hit":
                    card = self.deck.draw()
                    player.Hit(card)
                    time.sleep(1)
                    player.printCard(card)
                    player.addHand()
                    #player.#checkAce(card)
                    player.printTotal()
                    time.sleep(1)
                elif answer == "stand":
                    print("")
                    return False
                else:
                    print("Please enter a valid answer")

    
    def dealerTurn(self):
        while True:
            if self.dealer.checkBlackJack():
                self.winners.append(self.dealer)
                break
            elif self.dealer.total > 21:
                print("Dealer has bust!")
                print("")
                self.dealerBust = True
                break

            if self.dealer.total >= 17:
                print("The dealer stands!")
                break
            elif self.dealer.total <= 16:
                card = self.deck.draw()
                self.dealer.Hit(card)
                self.dealer.addHand()
                
                
                print("Dealer has drawn:")
                self.dealer.printCard(card)
                print("")
                time.sleep(1)
        self.checkWinners()



    def playRound(self):
        time.sleep(1)
        print("Dealers card:")
        self.dealer.printCard(self.dealer.hand[1])
        print("the other card is facing down!")
        time.sleep(1)
        for player in self.players:
            self.playTurn(player)
        time.sleep(1)
        print("Dealers cards:")
        self.dealer.printHand()
        time.sleep(1)
        self.dealerTurn()

        


    def checkWinners(self):
        dealer_total = self.dealer.addHand()

        if dealer_total > 21:
            for player in self.players:
                if player.addHand() <= 21:
                    print(player.name, "has won!")
                else:
                    print(player.name, "has also busted. It's a tie.")
            return True

        winning_players = []
        highest_value = 0
        for player in self.players:
            player_total = player.addHand()
            if player_total <= 21:
                if player_total > highest_value:
                    winning_players = [player]
                    highest_value = player_total
                elif player_total == highest_value:
                    winning_players.append(player)

        # Check the outcome
        if not winning_players:
            print("The dealer has won!")
        elif len(winning_players) == 1:
            print(winning_players[0].name, "has won!")
        else:
            print("It's a tie between the following players:")
            for player in winning_players:
                print(player.name)
        return True

        

        

    def nextRound(self):
            self.newRound()
            self.playRound()

        

        
        
        

                

                

    
            

        

    



            



