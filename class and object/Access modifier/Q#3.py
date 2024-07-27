class Movie:
    def __init__(self, title, director, release_year):
        self.__title = title
        self.__director = director
        self.__release_year = release_year


    def get_title(self):
        return self.__title

  
    def set_title(self, title):
        self.__title = title


    def get_director(self):
        return self.__director

 
    def set_director(self, director):
        self.__director = director


    def get_release_year(self):
        return self.__release_year

    def set_release_year(self, release_year):
        self.__release_year = release_year



movie = Movie("movie1", "director1", 2010)
print(f"""
    movie title: {movie.get_title() }         
    movie director:{movie.get_director() } 
    movie release year:{movie.get_release_year()}
""")
