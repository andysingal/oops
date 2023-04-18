# class Dog:
#     species = "Canis lupus"
#     def __init__(self,name,age,breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
class Movie:
    id_counter = 1
    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating
        Movie.id_counter+= 1


my_movie = Movie("Nomi", 4.5)
your_movie = Movie("Gomi", 4.7)

print(my_movie.id)
print(your_movie.id)