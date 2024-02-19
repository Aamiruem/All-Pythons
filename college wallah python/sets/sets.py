#  creating a set
names = {"Sia", "Mia", "Tia","Aaliya"}
# print(names)



# # check length of set
# print(len(names))


# # check data types of set
# print(type(names))


# # accessing items of set
# for x in names:
#     print(x)
    
    
    
# check if an items exists in a set
# if "Sia" in names:
    # print("Sia is in the set")
    
    
# ADD ELEMENTS IN SET
names.add("kamran")
# print(names)


# add another sequence in a set
names_list = ["Riya", "Kia"]
names.update(names_list)
# print(names)




# remove element from a set
names.remove("Tia")
# print(names)


# remove element from a set
names.discard("Ria") # this function will not throw an error if value is not present in the set
# print(names)




# joining  2 set
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}
# print(s1, s2)

s3 = s1.union(s2)
# print(s3)

s1.update(s2)
# print(s1)




# keep only duplicates while joining
s1.intersection_update(s2)
print(s1)



# keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)