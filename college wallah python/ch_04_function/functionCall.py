# write function that print hello worlds

def printHello():
    # body of function
    print("Hello Function!!")

# function call
printHello()




# function which takes 2  numbers as input and return their sum

def add(n1, n2=0):
    print("n1:", n2)
    print("n2:", n1)
    
    sum = n1+n2
    return sum

# positional arguments
# print("The sum is ", add(3,5))


# keyword argument (names arguments)
# print("The sum is ", add(n1 = 3, n2 = 5))


# default arguments
# print("The sum is ", add(3))


# arbitrary arguments
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum +=i
        return sum
    
output = addAllNumbers(1,2,3,4,5)
# print("The sum is ", output)



def studentInfo(**kwargs):
    for x, y in kwargs.items():
        print(x, "is",y)
        
studentInfo(name = "Aamir", age = 21, city = "Delhi", mob = "9931879953",)
studentInfo(name = "Kamran", age = 21, city = "Bangalore", mob = "9931879953",)
