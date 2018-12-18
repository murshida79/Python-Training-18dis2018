# TUPLE=LIST IMMUTABLE

tuple_a = ('a', 'a', 'b', 'c', 'a')
tuple_b = tuple()

print(bool(tuple_a))
print(bool(tuple_b))

tuple_c = (1, 2, 3)
tuple_d = 1

print(bool(tuple_c))
print(bool(tuple_d))

# TUPLE OPERATION

print(tuple_a.count('a'))
print(tuple_c.index(1))
print(tuple_a[0])

