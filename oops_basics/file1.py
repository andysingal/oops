# class Player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# player1 = Player(5, 6)
# player2 = Player(2, 4)
# player3 = Player(3, 6)
#
# players = [player1, player2, player3]
#
# for player in players:
#     print(f"X: {player.x} Y: {player.y}")
class Circle:
    def __init__(self,radius, color):
        self.radius = radius
        self.color = color

my_circle = Circle(6, "Yellow")

my_circle.radius = 5
print(my_circle.radius)
del my_circle.radius
print(my_circle.__dict__)
