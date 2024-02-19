# i = 0

# while i < 10:
    
#     i = i+1
#     print(i)



# i = 0

# while i < 20:
    
#     i = i+2
#     print(i)


try:
    # Taking input from the user for the value of n
    n = int(input("Enter a number (n) to generate the table: "))

    # Displaying the table from 1 to n
    print(f"Table from 1 to {n}:")
    print("Number |  Table")
    print("-" * 15)

    for i in range(1, n + 1):
        print(f"{i:6} |  {i * 2}")

except ValueError:
    print("Please enter a valid integer.")
