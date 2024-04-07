# Logical Operations => and, or, not, xor, not, in, not in, is, is not, is true, is false, is null, is not null, is not empty, is not null empty
# and, or, not, xor, not, in, not in, is, is not, is true, is false, is null, is not null, is not empty, is not null empty

a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a is b)

# and
print(True and True)  # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False

# or
print(True or True)  # Output: True
print(True or False)  # Output: True
print(False or True)  # Output: True

# not
print(not True)  # Output: False
print(not False)  # Output: True

# xor
print(True ^ True)  # Output: False
print(True ^ False)  # Output: True
print(False ^ True)  # Output: True
print(False ^ False)  # Output: False

# in
print('apple' in ['apple', 'banana', 'cherry'])  # Output: True
print('apple' not in ['apple', 'banana', 'cherry'])  # Output: False

# not in
print('apple' not in ['apple', 'banana', 'cherry'])  # Output: True
print('apple' in ['apple', 'banana', 'cherry'])  # Output: False

# is
print(5 is 5)  # Output: True
print(5 is not 5)  # Output: False

# is not
print(5 is not 5)  # Output: False
print(5 is not 10)  # Output: True

# is true
print(True is True)  # Output: True
print(True is False)  # Output: False

# is false
print(False is False)  # Output: True
print(False is True)  # Output: False

# is null
print(None is None)  # Output: True

# is not null
print(5 is not None)  # Output: True
print(None is not None)  # Output: False

# is not empty
print(None is not None)  # Output: False
print(None is not '')  # Output: True

# is empty
print('' is '')  # Output: True

# is not empty
print('' is not '')  # Output: False
print('' is not None)  # Output: True

# is not empty
print('' is not '')  # Output: False
print('' is not None)  # Output: False

# is not null empty
print(None is not None)  # Output: False
print(None is not '')  # Output: True

a = 10
b = 5
print(not False)
print(not (a > b))



val1 = True
val2 = False
print("ans operator ")
val3 = 0
val4 = 1