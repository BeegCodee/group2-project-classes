'''
Project Name: movie_library_management.py
Description: Python application that manages movie intentory and rental processes.
    Allows the user to add, update, remove, serach for, rent, and return movies.
    The application also allows the user to list movies by genre, list the top rented movies,
    check for movies' availability by genre, and display a summary of the movies' library.
Authors: Dylan Dang, Taylor Blair-Kril
Date: April 10, 2025
'''

import os
from movie import Movie

def load_movies(file_name):
    file_name = input('Enter the movie catalog filename: ')
    if not os.path.exists(file_name):
        print(f'The catalog file ({file_name}) is not found\nThe movie library management system starts without catalog')
        return []
    
    movies = []
    with open(file_name, 'r') as f:
        for line in f:
            movie_data = line.strip().split(',')
            if movie_data not in movies:
                movies.append(movie_data)
        return movies
    
print(load_movies('movies'))