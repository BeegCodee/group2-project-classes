'''
Project Name: movie_library_management.py
Description: Python application that manages movie intentory and rental processes.
    Allows the user to add, update, remove, serach for, rent, and return movies.
    The application also allows the user to list movies by genre, list the top rented movies,
    check for movies' availability by genre, and display a summary of the movies' library.
Authors: Dylan Dang, Taylor Blair-Kril
Date: April 19, 2025
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
    return None

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
    found_movies = []
    for movie in movies:
        if (search_term in movie.get_title().lower() or 
            search_term in movie.get_director().lower() or 
            search_term in movie.get_genre_name().lower()):
            found_movies.append(movie)
    return found_movies

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

def update_movie_details(movies):
    movie_id = input('Enter the movie ID to update: ')
    index = movie_index(movies, movie_id)
    if index != None:
        movie = movies[index]
        print('Leave fields blank to keep current values')
        new_title = input(f'Enter new title (current: {movie.get_title()}): ') or movie.get_title()
        movie.set_title(new_title)
        new_director = input(f'Enter new director (current: {movie.get_director()}): ') or movie.get_director()
        movie.set_director(new_director)
        new_genre = input(f'Enter new genre (current: {movie.get_genre()}): ') or movie.get_genre()
        movie.set_genre(new_genre)
        new_price = float(input(f'Enter new price (current: {movie.get_price()}): ')) or movie.get_price()
        movie.set_price(new_price)
        print(f"Movie with ID {movie_id}' is updated successfully.")
    else:
        print(f'Movie with ID {movie_id} is not found')

def add_movies(movies):
    movie_id = int(input('Enter movie ID: '))
    index = movie_index(movies, movie_id)
    if index != None:
        print(f'Movie with ID {movie_id} already exists') 

    else:
        title = input(f'Enter title: ').capitalize()
        director = input(f'Enter director: ').capitalize()
        genre = input(f'Enter genre: ').capitalize()
        price = float(input(f'Enter price: '))
        print(f'Movie {title} added successfully')

    new_movie = Movie(movie_id, title, director, genre, True, price)
    movies.append(new_movie)

def remove_movie(movies):
    movie_id = int(input('Enter the movie ID to remove: '))
    index = movie_index(movies, movie_id)
    if index != None:
        movie = movies[index] 
        removed_movie = movies[index]
        movies.remove(removed_movie)
        print(f"Movie '{movie.get_title()}' has been removed.")
    else:
        print(f'Movie with ID {movie_id} not found.')

def list_movies_by_genre(movies):
    genre_id = int(input(f'Enter genre (0-9): '))
    genre_name = Movie.GENRE_NAMES
    if genre_id > len(genre_name) or genre_id < 0:
        print('Invalid genre: Enter a valid genre (0-9)')
        return
    else:
        chosen_genre = Movie.GENRE_NAMES[genre_id].lower()
        matched_movies = []
        for movie in movies:
            if (chosen_genre in movie.get_genre_name().lower()):
                print(movie)

def top_rented_movies(movies):
    lambda movie: movie.get_rental_count()


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
    return None

#movie_index to help find a movie's index by ID
def movie_index(movies, movie_id):
    for i in range(len(movies)):
        if movies[i].get_id() == movie_id:
            return i
    return None

#main function that loads the file, displays the menu, and handles user interaction
def main():
    movies = load_movies('movie')
    file_name = 'movies.csv'
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
            
        if user_input == '4':
            added_movie = add_movies(movies)
            print(added_movie)

        if user_input == '5':
            removed_movie = remove_movie(movies)
            print(removed_movie)

        if user_input == '6':
            movie_update = update_movie_details(movies)
            print(movie_update)

        if user_input == '7':
            movie_genres = list_movies_by_genre(movies)
            print(movie_genres)

        print()
        user_input = print_menu()

    #Saves current movies to the catalog
    save = input('Would you like to update the catalog (yes/y, no/n)? ').lower()
    while (save != 'yes') or (save != 'y') or (save != 'no') or (save != 'n'):
        if (save == 'yes') or (save == 'y'):
            save_movies(file_name, movies)
            print('Movie catalog has been updated. Goodbye!')
            return None
        if (save == 'no') or (save == 'n'):
            print('Movie catalog has not been updated. Goodbye!')
            return None
        else:
            save = input('Invalid choice. Please choose (yes/y, no/n) ').lower()

if __name__ == "__main__":
    main()
