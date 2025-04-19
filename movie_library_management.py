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

#Loads movies from the csv file into a list
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

#When exiting the program, this function saves all movie changes to the csv file
def save_movies(file_name, movies):
    user_input = input('Would you like to update the catalog (yes/y, no/n)? ').lower()
    while user_input != 'no' or 'n':
        if user_input == 'yes' or 'y':
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
        else:
            print('Invalid selection. Please try again.')

#Main menu

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

    #Returns input as string
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

#Search for movies using title, director, or genre
def search_movies(movies, search_term):
    search_term = search_term.lower()
    matched_movies = []
    for movie in movies:
        if (search_term in movie.get_title().lower() or 
            search_term in movie.get_director().lower() or 
            search_term in movie.get_genre_name().lower()):
            matched_movies.append(movie)
    return matched_movies

#Rent a movie by ID
def rent_movie(movies, movie_id):
    index = movie_index(movies, movie_id)
    if index != None:
        movie = movies[index]
        if movie.get_available():
            movie.borrow_movie()
            return f"You have successfully rented '{movie.get_title()}'"
        else:
            return f"'{movie.get_title()}' is already rented."
    return f'Movie with ID {movie_id} not found.'

#Return a movie by ID
def return_movie(movies, movie_id):
    index = movie_index(movies, movie_id)
    if index != None:
        movie = movies[index]
        if not movie.get_available():
            movie.return_movie()
            return f"You have successfully returned '{movie.get_title()}'"
        else:
            return f"'{movie.get_title()}' was not rented."
    return f'Movie with ID {movie_id} not found.'

#Prints a list of movies
def print_movies(movies):
    if not movies:
        print('No matching movies found.')
        return
    
    print("    {:<10} {:<25} {:<21} {:<10} {:<17} {:<10} {:<10}".format("ID", "Title", "Director", "Genre", "Availability", "Price", "Rental Count"))
    print("-" * 120)
    
    for movie in movies:
        print("    {:<10} {:<25} {:<21} {:<10} {:<17} ${:<10.2f} {:<10}".format(
            movie.get_id(),
            movie.get_title(),
            movie.get_director(),
            movie.get_genre_name(),
            "Available" if movie.get_available() else "Rented",
            movie.get_price(),
            movie.get_rental_count()
        ))

#movie_index to help find a movie's index by ID
def movie_index(movies, movie_id):
    for i in range(len(movies)):
        if movies[i].get_id() == movie_id:
            return i
    return None

#main function that loads the file, displays the menu, and handles user interaction
def main():
    movies = load_movies('movie')
    user_input = print_menu()

    while user_input != '0':

        #Search for movie
        if user_input == '1':
            search_term = input('Enter search term: ')
            found_movies = search_movies(movies, search_term)
            print(f'Finding ({search_term}) in title, director, or genre...')
            if found_movies:
                print_movies(found_movies)
            else:
                print('No matching movies found.')

        #Rent a movie
        if user_input == '2':
            movie_id = input('Enter the movie ID to rent: ')
            rent = rent_movie(movies, movie_id)
            print(rent)

        #Return a movie
        if user_input == '3':
            movie_id = input('Enter the movie ID to return: ')
            movie_return = return_movie(movies, movie_id)
            print(movie_return)
            
        print()
        user_input = print_menu()

if __name__ == "__main__":
    main()