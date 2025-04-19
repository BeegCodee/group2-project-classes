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

#loads movies from the csv file into a list
def load_movies(file_name):
    file_name = input('Enter the movie catalog filename: ')  
    if not os.path.exists(file_name):
        print(f"File {file_name} not found. Starting with empty library.")
        return movies
    
    movies = []

    with open(file_name, mode='r') as file:
        for line in file:
            line = line.strip() 
            movie_data = line.split(',')
            movie_id = movie_data[0].strip()
            title = movie_data[1].strip()
            director = movie_data[2].strip()
            genre = int(movie_data[3])
            available = movie_data[4].strip().lower() == 'true'
            price = float(movie_data[5])
            movie = Movie(movie_id, title, director, genre, available, price)
            movies.append(movie)
    
    return movies

#test functionality (remove in the future)
print(load_movies('movies'))

#when exiting the program, this function saves all movie changes to the csv file
def save_movies(file_name, movies):
    with open(file_name, 'w') as file:
        for movie in movies:
            movie_data = [
                str(movie.get_id()),
                f'{movie.get_title()}',
                f'{movie.get_director()}',  
                str(movie.get_genre()),
                str(movie.get_available()).capitalize(),
                str(movie.get_price())
            ]
            file.write(','.join(movie_data) + '\n')