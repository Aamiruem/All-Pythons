# Slicing
# Accessing parts of a string
# str[ starting_idx: ending_idx] #ending idx is not included
# str = "ApnaCollege"
# str[ 1 : 4 ] is “pna”
# str[ :4] is same as str[ 0 : 4]
# str[ 1 ] is same as str[ 1 : len(str) ]


# Indexing index ↓ • position
# Apna Colege
# -
# 0 1 2 3 4 5 6 7 8 9 10 11
# str = "Apna_College"
# str[O] is 'A', str[1] is `p' ..
# str[0] = 'B' #not allowed


str = "Apna_College"

print(str[0:4])
print(str[5:len(str)])

# Slicing
# Negative Index
#  A  p  p  l  e
# -5 -4 -3 -2 -1
# str = "Apple"
# str[-3-1] is "pl"

str = "Apple"
print(str[-3:-1])  # -3 is the index of last character

# String Functions
# str = "I am a coder."
# str.endsWith("er.") #returns true if string ends with substr
# str.capitalize() #capitalizes 1st char
# str.replace( old, new) #replaces all occurrences of old with new
# str.find(word) #returns 1st index of 1st occurrence
# str.count("am") #counts the occurrence of substr in string


str = "i am a coder. and I am a programmer. of python"
print(str.find("am"))
print(str.replace("er", "ers"))
print(str.endswith("er."))
print(str.capitalize())
print(str.count("am"))

str = "I am a coder."
str = str.capitalize()
print(str)

# String Methods
str = "I am a coder."
str.lower()  # converts string to lower case
print(str.lower())  # returns a copy of the string with all uppercase letters converted to lower case.
str.upper()  # converts string to upper case
print(str.upper())  # returns a copy of the string with all lower case letters converted to upper case.)

# String Functions
str = "I am a coder."
print(str.endswith("er."))  # returns true if string ends with substr
print(str.capitalize())  # capitalizes 1st char
print(str.replace("er", "ers"))  # replaces all occurrences of old with new
print(str.find("am"))  # returns 1st index of 1st occurrence
print(str.count("am"))  # counts the occurrence of substr in string
print(str.lower())
