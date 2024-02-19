# def outer_function():
#     x = 1 # variable in the outer function
    
#     def inner_function():
#         y = 2 # variable in the inner function
#         result = x+y
#         return result
#     return inner_function()
# output = outer_function()

# print(output)




# pass by value 
def addOne(x):
    x = x+1
    print("inside function:", x)
    
    
x = 5
addOne(x)
print("Outside function:", x)




# pass by reference
def modifyList(lst):
    lst.append(4)
    print("Inside the function", lst)
lst = [1, 2, 3, 4]
modifyList(lst)
print("Outside the function: ", lst)