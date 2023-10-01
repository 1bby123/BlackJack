from Game import *

players = []
numOfPlayers = 0


print("Welcome to Blackjack!")
print("Press any key to continue")
input()

while True:
    try:
        numOfPlayers = int(input("How many players are playing?: "))
        break
    except ValueError:
        print("Please enter a valid number of players")

for player in range(numOfPlayers):
    name = input(f"Enter the name for Player {player + 1}: ")
    player = Player(name)
    players.append(player)

game = Game(players)

print("Players have been added, starting game...")
time.sleep(2)
game.newGame()





