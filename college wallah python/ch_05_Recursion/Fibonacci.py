# make a function which calculates fibonacci sequence using recursion.
def fibonacci(n):
    
    #  base case
    if n == 1:
        return 0
    elif n == 2: #base case
        return 1
    else:
        return "{0}{1}".format (fibonacci (n - 1), fibonacci (n - 2))  #recursive case
    
n = int(input("Enter n: "))
print(fibonacci(n))

for i in range(1, n+1):
    
    print(fibonacci(i))
