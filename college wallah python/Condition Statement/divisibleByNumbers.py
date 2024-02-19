num = int(input("Enter a positive number: "))

if num % 15 == 0:
    print("Number is divisible by 15: ")
    
else:
    if num % 3 == 0 or num % 5 == 0:
        print("Number is not divisible by 15 but divisible by 3 or 5 ")
    else:
        print("Number is neither divisible by 3 nor by 5")
    