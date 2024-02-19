# n1 = int(input("Enter number: "))
# n2 = int(input("Enter number: "))
# n3 = int(input("Enter number: "))


# if n1 > n2 and n1 >n3:
#     print(n1,"is the greatest number ")
    
# elif n2>n1 and n2> n3:
#     print(n2, "is the greatest number ")
    
# else:
#     print(n3, "is the greatest number ")





n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

if n1 > n2:
    if n1 > n3:
        print(n1, "is the greatest element")
    else:
        print(3, "is the greatest element")
        
else:
    if n2 > n3:
        print(n2, " is the greatest element")
    else:
        print(n3, "is the greatest element")
        
    # if n1 > n2:
    #     print(n1, "is the greatest element")
    # else:
    #     print(n2, "is the greatest element")