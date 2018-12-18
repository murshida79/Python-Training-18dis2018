dict_a = dict()  # if dist_a --> false

# DICT OPERATION

# Add key, value
dict_a['hello'] = 'world'

print(dict_a)
print(dict_a['hello'])
#print(dict_a['error'])

print(dict_a.get('error', 'Not found.'))

