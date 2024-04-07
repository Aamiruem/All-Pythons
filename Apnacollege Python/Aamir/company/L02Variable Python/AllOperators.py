# Types of operators
# 1.Assignment operators => (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)

# 2.Arithmetic operators => (+, -, *, /, %, //, **)

# 3.Comparison operators/relational operators => (==,!=, <, >, <=, >=, <=>)

# 4.Logical operators => (and, or, not)

# 5.Bitwise operators => ( &, |, ~, ^, >>, << )

# 6.Membership operators => (in, not in)

# 7.Identity operators => (is, is not)

# 8.Bitwise operators => (& and, | or, ^ not)

# 9.Operator Precedence => (()) [] .() ()[] {} . {} ** +x -x ~x **= <<= >>= &= |=) ^= >>= <<= >>= from left to right

# 10.Operator Associativity => (left to right, right to left)

# 11.Type conversion operators => (int, float, str, bool, complex)

# Actual operators precedence:

# 1. () [] . {}

# 2. **

# 3. * / % // divmod()

# 4. + - << >>

# 5. & | ^ ~

# 6. < > <= >= ==!= is is not in

# 7. and or not

# 8. in not in

# 9. is is not in



a = 2
b = 5

sum = a + b
print(sum)

# difference
a = 5
b = 9
diff = a - b
print(diff)

# product
a = 2
b = 3
prod = a * b
print(prod)

# quotient
a = 10
b = 2

quot = a / b
print(quot)

# remainder
a = 13
b = 3
rem = a % b
print(rem)

# exponentiation
a = 2
b = 3
exp = a ** b

print(exp)

# floor division
a = 10
b = 3
floor_div = a // b
print(floor_div)

# Assignment Operators
a = 10
a += 3  # a = a + 3
print(a)

a = 10
a -= 3  # a = a - 3
print(a)

a = 10
a *= 3  # a = a * 3
print(a)

a = 10
a /= 3  # a = a / 3
print(a)

a = 10
a %= 3  # a = a % 3
print(a)

a = 10
a **= 3  # a = a ** 3
print(a)

a = 10
a //= 3  # a = a // 3
print(a)
