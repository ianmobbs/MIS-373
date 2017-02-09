# 2. Movies.py

# Imported for Python 2 compatibility
# Must happen at beginning of file
from __future__ import print_function

# Imports
import csv
import sys

# Python 2 compatibility
if sys.version[0] == '2':
    input = raw_input

class MovieChecker:
    '''
    Student Group 7 - MovieChecker
    Bot that finds common actors between two movies using movies.csv
    '''
    def __init__(self):
        '''
        Loads movies.csv
        Welcomes user
        '''
        self.movies = {}
        with open('movies.csv', 'r') as file:
            for row in file:
                row = row.strip().split(',')
                actor = row[0]
                actorMovies = row[1:]
                for movie in actorMovies:
                    if movie in self.movies:
                        self.movies[movie].append(actor)
                    else:
                        self.movies[movie] = [actor]
        print("Welcome to movie checker!")
        print("Enter the name of any two movies to find common actors.")
        print("You can also type \"Quit\" at any time to leave.")
        self.checkMovies()

    def movieInput(self, text):
        '''
        Given text, returns sanitized input
        '''
        while True:
            movie = input(text).strip().title()
            if movie in self.movies:
                return movie
            elif movie == "Quit":
                return False
            else:
                print("Sorry, we don't have that movie in our database.")

    def compareMovies(self, m1, m2):
        '''
        Given two movies, finds:
            - Common actors between the two
            - Exclusive actors for both movies
        Returns sets
        '''
        commonActors = set(m1) & set(m2)
        movie1Actors = set(m1) - set(m2)
        movie2Actors = set(m2) - set(m1)
        return commonActors, movie1Actors, movie2Actors

    def checkMovies(self):
        '''
        Kernel
        Prompts user for movies, returns common actors
        '''
        movie1 = self.movieInput("Movie 1: ")
        if not movie1:
            print("Goodbye!")
            return
        movie2 = self.movieInput("Movie 2: ")
        if not movie2:
            print("Goodbye!")
            return
        commonActors, movie1Actors, movie2Actors = self.compareMovies(self.movies[movie1], self.movies[movie2])
        print("Common actors between {0} and {1}:".format(movie1, movie2), ", ".join(commonActors))
        print("Actors exclusive to {0}:".format(movie1), ", ".join(movie1Actors))
        print("Actors exclusive to {0}:".format(movie2), ", ".join(movie2Actors))

        print("Goodbye!")

if __name__ == '__main__':
    m = MovieChecker()
