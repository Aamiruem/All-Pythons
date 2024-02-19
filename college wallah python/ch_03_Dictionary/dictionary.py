# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionaries items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# phones = {
#     "john": 993187,
#      "Ria": 897543,
#      "Joy": 1312678
# }
# #  printing the dictionary
# print(phones)


# # checking the type of dictionary
# print(type(phones))

# # check the length of dictionary
# print(len(phones))


# # access items of dictionary
# print(type("john"))
# print(phones.get("john"))
# print(phones.keys())


# # update value in dic
# phones["john"] = 98767566
# print(phones)



# # add elements in dict
# phones["joy"] = 9786746
# print(phones)



# more_phones = {
#     "kia": 2344564
# }

# phones.update(more_phones)
# print(phones)


# # remove elements i a dictionary
# phones.pop("john")
# print(phones)

# phones.popitem() # this will remove the last added items
# print(phones)


# phones.clear() #this will empty the dictionary
# print(phones)


# #  printing value of a dictionary
# for x,y in phones.items():
#     print(x,y)
    
    
    
    
    
# Nested Dictionary
phones = {
"Area1":{
    "x": 0,
    "y": 1,
    "z": 2,

    },
    "Area2":{
    "a": 3,
    "b": 4,
    "c": 5,
    }
}

print(phones["Area1"]["y"])
print(phones["Area2"]["c"])