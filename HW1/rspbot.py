from operator import itemgetter

class RockPaperScissorsBot:
	def __init__(self):
		self.opponentMoves = {
			"Rock":0,
			"Paper":0,
			"Scissors":0
		}
		self.winningMoves = {
			"Rock":"Paper",
			"Paper":"Scissors",
			"Scissors":"Rock"
		}
		print("Welcome to Rock Paper Scissors bot!")
		print("You can play by typing \"Rock\", \"Paper\", or \"Scissors\".")
		print("You can also type \"Quit\" at any time to leave.")
		self.play()

	def gameInput(self, text):
		move = input(text).lower()
		if move == "rock":
			self.opponentMoves["Rock"] += 1
			return "Rock"
		elif move == "paper":
			self.opponentMoves["Paper"] += 1
			return "Paper"
		elif move == "scissors":
			self.opponentMoves["Scissors"] += 1
			return "Scissors"
		elif move == "quit":
			return False
		else:
			return self.gameInput("Sorry, I didn't get that.\n{0}".format(text)) 

	def pickMove(self):
		likelyMove = sorted(self.opponentMoves.items(), key=itemgetter(1))[::-1][0][0]
		moveToPlay = self.winningMoves[likelyMove]
		return moveToPlay

	def chooseWinner(self, player, bot):
		if player == bot:
			return "It's a tie!"
		elif self.winningMoves[player] == bot:
			return "I won!"
		else:
			return "You win!"

	def play(self):
		while True:
			botMove = self.pickMove().title()
			move = self.gameInput("What's your move? ").title()
			if not move:
				break
			winner = self.chooseWinner(move, botMove)
			print("I chose {0}.".format(botMove.lower()))
			print(winner)
		print("Goodbye!")
		return
	
if __name__ == '__main__':
	bot = RockPaperScissorsBot()