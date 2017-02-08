# Imports
from operator import itemgetter

# Rock Paper Scissors Bot
class RockPaperScissorsBot:
	'''
	Ian Mobbs - im6293 - Rock Paper Scissors Bot
	Bot designed to play Rock Paper Scissors with
	Tracks all moves made my player and chooses best move based on their move history
	'''
	def __init__(self):
		'''
		Initializes bot
		Loads empty dictionary of enemy moves played
		Stores winning moves based on enemy move
		Starts gameplay
		'''
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
		'''
		Special input handler to log user moves
		Given text to prompt with, returns sanitized input
		'''
		while True:
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
				print("Sorry, I didn't get that.")
				print("You can play by typing \"Rock\", \"Paper\", or \"Scissors\".")
				print("You can also type \"Quit\" at any time to leave.")

	def pickMove(self):
		'''
		Finds most played move of other player
		Returns best counter to that move
		'''
		likelyMove = sorted(self.opponentMoves.items(), key=itemgetter(1))[::-1][0][0]
		moveToPlay = self.winningMoves[likelyMove]
		return moveToPlay

	def chooseWinner(self, player, bot):
		'''
		Given two moves, returns a string that declares who won
		'''
		if player == bot:
			return "It's a tie!"
		elif self.winningMoves[player] == bot:
			return "I won!"
		else:
			return "You win!"

	def play(self):
		'''
		Runs game until user decides to quit
		'''
		while True:
			botMove = self.pickMove().title()
			move = self.gameInput("What's your move? ").title()
			if not move:
				break
			winner = self.chooseWinner(move, botMove)
			print("I chose {0}.".format(botMove.lower()))
			print(winner)
			print("-----")
		
		print("Goodbye!")
		return
	
if __name__ == '__main__':
	bot = RockPaperScissorsBot()