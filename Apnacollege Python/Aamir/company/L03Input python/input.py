# input => from user input => string => string.split(' ')    => split the string by space and return it as an array => split(' ') => split the string by space and return it as an array
# output => from user input => string => string.split(' ')    => split the string by space and return it as an array => split(' ') => split the string by space and return it as an array
#
# => split(' ') => split the string by space and return it as an array => split(' ') => split the string by space and return it as an array


# Taking input from the users
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
price = float(input("Enter the price: "))

# Printing the input values
print("Name: ", name)
print("Age: ", age)
print("City: ", city)
print("Price: ", price)

print("Input values: ", "My Name is", name, "I am", age, " years old, I live in",  city, "and room rent is", price, "per month")