a = set()  # create an empty set
print(type(a))

b = {1, 2, '3'}  # even for the set we use curly brackets
print(b)
print(type(b))

dict_1 = {1: '1', 9: 'nove', 'key_tre': 3}

set1 = set(dict_1)  # set method
print(set1)

set2_values = set(dict_1.values())
print(set2_values)

set2_values.add("another element")
print(set2_values)  # set is not ordered

set3 = {"another element"}
print(set2_values.difference(set3))  # differece method

print(set2_values.intersection(set3))   #intersection method

print(set2_values.isdisjoint(set3)) # isdisjoint method