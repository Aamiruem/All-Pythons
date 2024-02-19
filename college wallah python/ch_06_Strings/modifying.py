name1 = 'college wallah'

name2 = "physics wallah"

name3 = '''iit 
wallah'''

# for converting characters to uppercase
str1 = "New york"
str2 = str1.upper()
# print(str2)


# for converting characters to lowercase
str3 = str2.lower()
# print(str3)


# for capitalising the first characters of my string
str4 = str3.capitalize()
# print(str4)


# for stripping/removing any trailing string whitespace
str1 = "Hello Aamir!"
print(str1.strip())
# print(str1)


# replace substring
str1 = "Hello world, what a beautiful world this is!"
# print(str1.replace("world", "earth", 1))



# split() function
# splitting string 
str1 = " ria pia sia tia mia "
list = str1.split(",")
# print(list)


# concatenation
str1 = "Hello kamran!"
str2 = "what a great place this is."
print(str1 + str2)

# string formatting
student_name = "Pallavi"
student_marks = 98

str1 = "The student name is {s}, and marks is {m}". format(s = student_name, m = student_marks)
print(str1)