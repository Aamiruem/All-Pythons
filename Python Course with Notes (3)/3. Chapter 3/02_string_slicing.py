greeting = "Good Morning, "
name = "Aamir"
print(type(name))

# Concatenating two strings
c = greeting + name
print(c)
name: str = "Aamir"
print(name[4])
# name[3] = "d" --> Does not work

print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
c = name[-4:-1] # is same is name[1:4]
print(c)

name1 = "AamirIsGood"
d = name[0::3]
d = name[1:4:1]
d = name[1:4:2]
d1: str = name[:0:-1]
print(d)
