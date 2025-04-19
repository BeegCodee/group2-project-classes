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
        print(f"The catalog file ({file_name}) is not found\nThe movie library management system starts without catalog.")
        return []
    
    movies = []

    with open(file_name, mode='r') as file:
        for line in file:
            line = line.strip() 
            movie_data = line.split(',')
            movie_id = movie_data[0].strip()
            title = movie_data[1].strip()
            director = movie_data[2].strip()
            genre = int(movie_data[3])
            available = movie_data[4].strip().capitalize() == 'True'
            price = float(movie_data[5])
            movie = Movie(movie_id, title, director, genre, available, price)
            movies.append(movie)
    
    return movies

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

#main menu

def print_menu():
    print('Movie Library - Main Menu')
    print('=' * 25)
    print('1) Search for movies')
    print('2) Rent a movie')
    print('3) Return a movie')
    print('4) Add a movie')
    print('5) Remove a movie')
    print('6) Update movie details')
    print('7) List movies by genre')
    print('8) Top rented movies')
    print('9) Check availability by genre')
    print('10) Display library summary')
    print('0) Exit the system')

    #returns input as string
    user_input = input('Enter your selection: ')
    while user_input != '0':
        if user_input == '1':
            return user_input
        if user_input == '2':
            return user_input
        if user_input == '3':
            return user_input
        if user_input == '4':
            return user_input
        if user_input == '5':
            return user_input
        if user_input == '6':
            return user_input
        if user_input == '7':
            return user_input
        if user_input == '8':
            return user_input
        if user_input == '9':
            return user_input
        else:
            print('Invalid choice. Please try again')
            user_input = input('Enter your selection: ')
    return user_input