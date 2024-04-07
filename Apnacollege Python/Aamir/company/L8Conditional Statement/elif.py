# light = "green"
#
# if (light == "green"):
#     print("Go")
# elif (light == "yellow"):
#     print("Look")
# elif (light == "red"):
#     print("Stop")
# else:
#     print("Invalid input")
#


light = input("Please enter the color of the light? ")
light = light.lower()

if (light == "green"):
    print("Go")
elif (light == "yellow"):
    print("Look")
elif (light == "red"):
    print("Stop")
else:
    print("Invalid input")




num = 10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



num = 5

if (num > 2):
    print("Num is greater than 2")

elif (num == 2):
    print("Num is equal to 2")

else:
    print("Num is less than 2")

    