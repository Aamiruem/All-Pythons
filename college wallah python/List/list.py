#  creating a tuple

colors = ("red", "yellow", "green")

# creating a tuple with 1 item
# fruit = ("apple")
fruits = tuple("apple")

# # check type of tuple
# print(type(colors))


# # check length of tuple
# print(len(colors))

# # accessing items in the tuples
# print(colors[1]) # positive index
# print(colors[-1]) # negative index

# print(colors[1:3]) # range indexing

# print(colors[-2:]) # negative range indexing 


# #  check if an item exist in tuple
# if "green" in colors:
#     print("Green is part of tuple ")


# # traverse the tuples
# for i in colors:
#     print(i)
    
    
#  concatenate 2 tuples
more_colours = ["blue", "brown"]
# colors = colors + more_colours
# print(colors)


#  unpacking a tuple
colours1, colours2, colours3 = colors
# print(colours1, colours2, colours3 )




#  reverse tuples
tuples = (10, 11, 12, 13, 14, 15)

list = []

for x in reversed(tuples):
    list.append(x)


output_tuple = tuple(list) # type cast into tuples
print(output_tuple)