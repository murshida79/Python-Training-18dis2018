# LIST IS MUTABLE
list_a = []
list_b = list()

# print(len(list_a))
# print(len(list_b))

# LIST COMPREHENSION
list_c = [1, 2, 3, 4, 5]
list_c2 = [6, 7, 8]
list_d = [i*2 for i in list_c]
list_c.extend(list_c2)
print(list_c)

# LIST OPERATION

empty_list = []
empty_list.append('a')
empty_list.append('b')

print(empty_list)
