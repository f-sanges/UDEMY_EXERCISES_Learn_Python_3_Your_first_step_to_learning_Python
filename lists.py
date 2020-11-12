a = "abcd"
b = list(a)  # create a list starting from a string
print(b)

birthday = "21/07/1982"
c = list(birthday)
print(c)

d = birthday.split('/')
print(d)

e = ['1', '2']
e.append(3)
print(e)

e.insert(1, "other number")  # insert
print(e)

e.remove("other number")  # remove
print(e)

e.pop(2)  # pop
print(e)

del e[1]  # del
print(e)

e.clear()  # clear
print(e)

list1 = ["Abba", "ACDC", "Aerosmith", "ACDC"]
print(list1.index("Aerosmith"))  # index
print("ACDC" in list1)  # in
print(list1.count("ACDC"))  # count
print(sorted(list1))  # sort
print(sorted(list1))

numbers = [1, 4, 3, 9, 7]
numbers.sort()              #sort
print(numbers)
numbers.sort(reverse=True)  #sort reverse
print(numbers)

s=[10,20,30]
n=s                     #n and s point to the same memory location
s[0] = "changed"
print(s)
print(n)
t = s.copy()                #copy
print("t copy of s: ", t)
s[0] = "changed again"
print("t does non change:", t)
print("s: ", s)


# Convert a list to a tuple
list1=["uno", "due", 3]
tup1 = tuple(list1)             #tuple command
print("type of list1", type(list1))
print("type of tup1", type(tup1))

list2 = list(tup1)          # list command
print(list2)