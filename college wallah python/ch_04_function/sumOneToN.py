# writing a function for calculating sum from 1 to n
def sumOneToN(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i
    return sum

n = int(input("Enter n: "))
# call function
output = sumOneToN(n)
print("sum of all numbers till n is",output)    



n1 = int(input("Enter n: "))
# call function
output1 = sumOneToN(n1)
print("sum of all numbers till n is",output1)    