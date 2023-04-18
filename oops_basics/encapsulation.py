class Movie:
    id_counter = 1
    def __init__(self,title,year, language,rating):
        self._id = Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter += 1

my_movie = Movie("Pride and Prejuidice", 2005, "English", 4.7)
your_movie = Movie("Sense and Sensibility", 1995, "English", 4.6)


print(my_movie._id)
print(your_movie._id)
