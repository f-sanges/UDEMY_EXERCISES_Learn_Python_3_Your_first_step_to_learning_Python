stringa = "ciao"
print("Initial string: ", stringa)

stringa_mod = stringa.replace('c', 'm', 1)
print("Modified string: " + stringa_mod)

stringa_added = "CI" + stringa[2:4]     # concatenate string and slice of another string
print("stringa_added: " + stringa_added)

print(stringa_added[1:len(stringa_added):2])    # print slice of stringa_added with step 2

# split
stringa_new = "uno, due, tre"
stringa_new_splitted = stringa_new.split(',')
print("stringa_new_splitted: ", stringa_new_splitted)
print("type of stringa_new_splitted: ", type(stringa_new_splitted))

# join
string_joined = ','.join(stringa_new_splitted)
print("string_joined: " +string_joined)
print("type of string_joined: ", type(string_joined))
