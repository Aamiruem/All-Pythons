# Strings
# String is data type that stores a sequence of characters.
# Basic Operations
# • concatenation
# "hello" + "world" "helloworld"
# ● length of str
# len(str)


# Str1 = "This is a String"
# Str2 = 'Apnacollege'
# str3 = """
# This is a multiline string."""
#
# print(Str1)
# print(Str2)
# print(str3)

# Escape Sequences
# \n \t \b \f \r
# \' \" \? \a \v \f \n \r \t


# str = "This is a \n newline character."
# print(str)

# String Indexing
# Strings are arrays of characters
# Indexing starts from 0
# Negative indexing is also supported (-1, -2, -3)





# lecture_two.py
# lecture_two.py > ...

# str1 = "apna"
# len1 = len(str1)
# print(len1)
#
# str2 = "college"
# len2 = len(str2)
# print(len2)
#
# final_str = str1 + " " + str2
# print(final_str)
#
# print(len(final_str))


# WAP to find the occurrence of '$' in a string.

str = "I have $10000 in my$ bank $ account$."

count = 0

for i in range(len(str)):
    if str[i] == "$":
        count += 1
print("The number of '$' in the string is :", count)