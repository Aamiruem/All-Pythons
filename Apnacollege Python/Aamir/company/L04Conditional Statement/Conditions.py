# condition = True if condition else False

# if => the condition is true
# else => the condition is false
# elif => the condition is false

# Traffic Light problem with codes
"""
light: str = input("Enter the color of the traffic light: ")
if(light == "red"):
    print("Stop")
elif(light == "Yellow"):
    print("lookout for cars")

elif(light == "green"):
    print("Go")
else:
    print("Invalid input")
    """

# Grade of student problem with codes

# marks: int = int(input("Enter the grade of the student: "))
# if (marks >= 90):
#     print("A")
# elif (marks >= 80 and marks < 90):
#     print("B")
# elif (marks >= 70 and marks < 80):
#     print("C")
# elif (marks >= 60 and marks < 70):
#     print("D")
# else:
#     print("F")

"""
num: int = int(input("Enter a number: "))

if(num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")
    """

# Write a program to check if a year is a leap year or not

# """
# year: int = int(input("Enter a year: "))
#
# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("The year is a leap year")
#         else:
#             print("The year is not a leap year")
#             """


# A = 5 & G = M
# A = 2 & G = F

# A = int(input("Enter the value of A: "))
# G = input("Enter the value of M/F: ")
#
# if (A == 1 or A == 2) and G == "M":
#     print("fee is 100")
# elif A == 3 or A == 4 or G == "F":
#     print("fee is 200")
# elif A == 5 and G == "M":
#     print("fee is 300")
# else:
#     print("No fee")


# Ternary operator => condition_is_true if condition else condition_is_false    if condition is true then print "Yes" else print "No"
# single line if Ternary operator
# print("Yes" if A == 1 else "No")
# <var> = <val1> if <condition> else <val2>


food = input("Enter your favourite food: ")

if food == "pizza":
    print("You chose pizza")
else:
    print("You chose something else")
eat = "yes" if food == "pizza" else "no"
print(eat)

# <stt1> if <condition> else <stt2>
food = input("Enter your favourite food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("no sweet")

# <var> = (false_val, true_val)[condition]

age = int(input("Enter your age: "))
vote = ("yes", "no")[age >= 18]
print(vote)  

sal = float(input("Enter your salary: "))
tax = sal * (0.1, 0.2)[sal >= 50000]
print(tax)
