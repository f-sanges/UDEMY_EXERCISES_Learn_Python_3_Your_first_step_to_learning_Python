a = {}
print(type(a))

list1 = [[1, 'uno'], [2, 'due'], [3, 'tre']]

b = dict(list1)  # dict command to transform a list into dictionary
print(b)

a = {1: 'A1', 2: 'B2', 3: 'C3', 1: 'D4'}  # if i define twice a key, the last will overwrite it (1 in the ex)
print(a)

b = {'5': "E5", 1: 'E6'}

a.update(b)  # update method
print(a)  # note that b has 1:'E6' that will replace the value in key 1

del a[1]  # delete the element with key 1
print(a)

print(a.get(2))     #get method to take the value of the key 2; same effect of a[2]
print(a.keys())     # keys method
list1 = list(a.keys())  # put the keys of the dictionary in a list
print(list1)
print(a.values())   #values method

new_dict = a.copy()
print("new_dict: ",new_dict )   # copy method
print(new_dict.items())     # items method
print(new_dict.pop(3))  # pop method; if you do not specify the key
new_dict.popitem()  # popitem method; it removes the last element
print(new_dict)


a.clear()  # clear method
print(a)  # all elements removed
