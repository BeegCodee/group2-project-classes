class Movie:

    GENRE_NAMES = {
        0 : 'Action', 
        1 : 'Comedy', 
        2 : 'Drama', 
        3 : 'Horror', 
        4 : 'Sci-Fi', 
        5 : 'Romance',
        6 : 'Thriller', 
        7 : 'Animation', 
        8 : 'Documentary', 
        9 : 'Fantasy'
}

    def __init__(self, movie_id, title, director, genre, available, price = 0.0, fine_rate = 0.0):
        self.__id = movie_id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__fine_rate = fine_rate
        self.__rental_count = 0

    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_director(self):
        return self.__director
    
    def get_genre(self):
        return self.__genre
    
    def get_available(self):
        return self.__available
    
    def get_price(self):
        return self.__price
    
    def get_fine_rate(self):
        return self.__fine_rate
    
    def get_rental_count(self):
        return self.__rental_count
    
    def get_genre_name(self):
        return self.GENRE_NAMES.get(self.__genre, 'Unknown')
    
    def get_availability(self):
        if self.__available == True:
            return 'Available'
        else:
            return 'Rented'
        
    def set_id(self, movie_id):
        self.__id = movie_id

    def set_title(self, title):
        self.__title = title

    def set_director(self, director):
        self.__director = director

    def set_genre(self, genre):
        self.__genre = genre

    def set_price(self, price):
        self.__price = price

    def set_fine_rate(self, fine_rate):
        self.__fine_rate = fine_rate

    def borrow_movie(self):
        self.__available = False
        self.__rental_count += 1

    def return_movie(self):
        self.__available = True

    def __str__(self):
                return (f'    'f"{self.__id:<17} {self.__title:<25} {self.__director:<21} " f"{self.get_genre_name():<10} {self.get_availability():<17} " f"${self.__price:<10.2f} {self.__rental_count}")