# 1. Rock Paper Scissors

# Imported for Python 2 compatibility
# Must happen at beginning of file
from  __future__ import print_function

# Imports
import sys
from operator import itemgetter

# Python 2 compatibility
if sys.version[0] == '2':
	input = raw_input

# Rock Paper Scissors Bot
class RockPaperScissorsBot:
	'''
	Student Group 7 - Rock Paper Scissors Bot
	Rock Paper Scissors bot that tracks all moves made my player and chooses best move based on their move history
	'''
	def __init__(self):
		'''
		Initializes bot
		Loads empty dictionary of enemy moves played
		Stores winning moves based on enemy move
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

		self.gamesPlayed = 0
		self.gamesUserWon = 0

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
			move = input(text).title().strip()
			if move in ["Rock", "Paper", "Scissors"]:
				self.opponentMoves[move] += 1
				return move
			elif move == "Quit":
				return False
			else:
				print("Sorry, I didn't get that.")
				print("You can play by typing \"Rock\", \"Paper\", or \"Scissors\".")
				print("You can also type \"Quit\" at any time to leave.")

	def pickMove(self):
		'''
		Finds most played move of other player and returns best counter to that move
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
			self.gamesUserWon += 1
			return "You win!"

	def play(self):
		'''
		Runs game until user decides to quit
		'''
		while True:
			botMove = self.pickMove()
			move = self.gameInput("What's your move? ")
			if not move:
				break
			self.gamesPlayed += 1
			winner = self.chooseWinner(move, botMove)
			print("I chose {0}.".format(botMove.lower()))
			print(winner)
			print("-----")
		print("You played {0} games, and won {1} of them.".format(self.gamesPlayed, self.gamesUserWon))
		print("Goodbye!")
		return

if __name__ == '__main__':
	bot = RockPaperScissorsBot()
