def remove_even_values(dictionary):
    for key,value in dictionary.copy().items():
        if value % 2 == 0:
            del dictionary[key]

my_dictionary = {"a":1, "b": 2, "c": 3, "d": 4}
remove_even_values(my_dictionary)
print(my_dictionary)
# class WaitingList:
#
#     def __init__(self, clients=None):
#         if clients == None:
#             self.clients = []
#         else:
#             self.clients = clients
#
#     def add_client(self, client):
#         self.clients.append(client)

# a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
# b = a
# c = b
# b = c
#
# def remove_elem(data, target):
# 	new_data = data[:]
#
# 	for item in data:
# 		if item == target:
# 			new_data.remove(target)
#
# 	return new_data
#
# def get_product(data):
# 	total = 1
#
# 	for i in range(len(data)):
# 		total *= data[i]
#
# 	return total
#
# remove_elem(c, 3)
# print(get_product(b))
# print(a)
