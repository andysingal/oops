class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter...")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating")

movie = Movie("Titanic", 4.3)
print(movie.rating)

movie.rating = -5.6
print(movie.rating)