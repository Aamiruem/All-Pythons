# n = int(input("Enter a number n:"))

# for _ in range(n):
#     print("*" * 5)
    
    
    
    
# n = int(input("Enter a number n:"))

# for i in range(n): #loop for rows
#     for j in range(1, n + 1): #loop for columns
#         print(j, end = "")
#     print()
    
    
    
    
    
# n = int(input("Enter a number n:"))

# for i in range(1, n+1): #loop for rows
#     for j in range(1, i+1): #loop for columns
#         print(j, end = "")
#     print()
    

# # outer loop
# for i in range (65,70):
#     # inner loop
#     for j in range(65,i+1):
#         print(chr(j),end="")
#     print()
# # OUTPUT:-
# # A
# # AB
# # ABC
# # ABCD
# # ABCDE


# for i in range (65, 70):
#     # inner loop
#     for j in range(65, i+1):
#         print(chr(i), end="")
#     print()

# # output:-    
# # A
# # BB
# # CCC
# # DDDD
# # EEEEE
    
    
# # Outer loop
# for i in range(65,70):
#     k=i
#     # Inner loop
#     for j in range(65,i+1):
#         print(chr(k),end="")
#         k=k+1
#     print()
# # Output:-

# # A
# # BC
# # CDE
# # DEFG
# # EFGHI


# str= "AAMIR"  # string
# # Outer loop
# for i in range(0,5):
#     # inner loop
#     for j in range(0,i+1):
#         print(str[j],end="")
#     print()
    
# # OUTPUT:-
# # A
# # AA
# # AAM
# # AAMI
# # AAMIR


# # Outer loop
# for i in range(65,70):
#     # Inner loop
#     for j in range(i,64,-1):
#         print(chr(j),end="")
#     print()
    
    
    
    
# m=6   
# # Outer loop
# for i in range(65,70):
#     m=m-1
#     # Inner loop 1 
#     for j in range(m,1,-1):
#         print(" ",end="")
#     # Inner loop 2
#     for k in range(65,i+1):
#         print(chr(k),end="")
#     # Inner loop 3
#     for n in range(65,i):
#         print(chr(n),end="")
#     print()
    
# #     A
# #    ABA
# #   ABCAB
# #  ABCDABC
# # ABCDEABCD





# # Outer loop
# for i in range(65,70):
#     # Inner loop
#     for j in range(i,64,-1):
#         # print(" ",end="")
#         print(chr(j),end="")
#     print()
    
    
    
    
 
# # Set the range for the outer loop
# for i in range(65, 70):
#     # Inner loop 1: Print white spaces
#     for j in range(69, i, -1):
#         print(" ", end="")
    
#     # Inner loop 2: Print alphabetic pattern
#     for k in range(65, i + 1):
#         print(chr(k), end="")
    
#     # Move to the next line after printing the pattern for each row
#     print()




# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")
# print()


# # AABABCABCD



# # Outer loop
# for i in range(65,70):
#     # Inner loop
#     for j in range(i,64,-1):
#         print(chr(j),end="")
#     print()
    
# # A
# # BA
# # CBA
# # DCBA
# # EDCBA


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),(str(chr(64+i)+" "))*(2*i-1))
    
    
# # Enter the number of rows: 5
# #      A 
# #     B B B 
# #    C C C C C 
# #   D D D D D D D 
# #  E E E E E E E E E 



# num=int(input("Enter a number:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(chr(65+num-j),end=" ")
#     print()
# for a in range(1,num+1):
#     for k in range(num-a,0,-1):
#         print(chr(64+k+a),end=" ")
#     print()
    
    
# Enter a number:10
# J 
# J I 
# J I H 
# J I H G 
# J I H G F 
# J I H G F E 
# J I H G F E D 
# J I H G F E D C 
# J I H G F E D C B 
# J I H G F E D C B A 
# J I H G F E D C B 
# J I H G F E D C 
# J I H G F E D 
# J I H G F E 
# J I H G F 
# J I H G 
# J I H 
# J I 
# J




# num=int(input("Enter a number:"))
# for i in range(1,num+1):
#     print(" "*(i-1),end="")
#     for j in range(1,num+2-i):
#         print(chr(65+num+1-i-j),end=" ")
#     print()
    
    
# Enter a number:10
# J I H G F E D C B A 
#  I H G F E D C B A 
#   H G F E D C B A 
#    G F E D C B A 
#     F E D C B A 
#      E D C B A 
#       D C B A 
#        C B A 
#         B A 
#          A 




# num=int(input("Enter a number:"))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()
# for p in range(1,num):
#     print(" "*p,end="")
#     for q in range(1,num+1-p):
#         print(chr(64+q+p),end=" ")
#     print()
    
    
# Enter a number:8
#        A 
#       A B 
#      A B C 
#     A B C D 
#    A B C D E 
#   A B C D E F 
#  A B C D E F G 
# A B C D E F G H 
#  B C D E F G H 
#   C D E F G H 
#    D E F G H 
#     E F G H 
#      F G H 
#       G H 
#        H




# # A given value of N will produce (2 * N - 1) rows, of which the first N rows
# # will be unique and the remaining (N - 1) rows will be mirrored
# num_rows = 5
# # The code of the starting character
# start = 65

# # Produce N unique rows: first row has one character, all others have two
# rows = [chr(start)] + [f"{chr(start + 2 * i + 1)} {chr(start + 2 * i + 2)}"
#                        for i in range(num_rows - 1)] if num_rows > 0 else []
# # Produce (N - 1) mirrored rows by reversing everything but the last row,
# # join with line breaks, then print
# print("\n".join(rows + rows[-2::-1]))


# # A
# # B C
# # D E
# # F G
# # H I
# # F G
# # D E
# # B C
# # A



# # outer loop for ith rows
# for i in range (65,70):
#     # inner loop for jth columns
#     for j in range(65,i+1):
#         print(chr(i),end="")
#     print()
    
    



asciichr = 65

# outer loop for ith rows
for i in range(0,6):
    # inner loop for jth columns
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()
    
# A
# BC
# DEF
# GHIJ
# KLMNO
# PQRSTU




rows=5
# outer loop for ith row
for i in range (1,rows+1):
    asciichr = 65
    for space in range(rows-i): 
       print(' ',end=' ')
    # inner loop for jth columns
    for j in range(1, 2*i):
        char = chr(asciichr)
        print(char+' ' ,end="")
        asciichr += 1

    print()

#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I






rows = 5
num = rows
asciichr = 65

# outer loop for ith rows
for i in range(rows, 0, -1):
    # inner loop for jth columns
    for j in range(0, i):
        char = chr(asciichr)
        print(char+' ' ,end="")
        asciichr += 1
    print("\r")





rows=5
# outer loop for ith row
for i in range (1,rows+1):
    asciichr = 65
    for space in range(rows-i): 
       print(' ',end=' ')
    # inner loop for jth columns
    for j in range(1, 2*i):
        char = chr(asciichr)
        print(char+' ' ,end="")
        asciichr += 1

    print()
    
    
    
    
    
    
    
ows = 5
num = rows
asciichr = 65

# outer loop for ith rows
for i in range(rows, 0, -1):
    # inner loop for jth columns
    for j in range(0, i):
        char = chr(asciichr)
        print(char+' ' ,end="")
        asciichr += 1
    print("\r")
    
    
    
    
    
rows = 6
asciichr = 65
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        char = chr(asciichr)
        print(char+' ' ,end="")
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(char, '', end='')
    print('\n')
    asciichr += 1 
    
    
# A A A A A A A A A A

# B B B B     B B B B

# C C C         C C C

# D D             D D

# E                 E
   




# Upper triangle shape
upper =5
# outer loop for ith row
for i in range (1,upper+1):
    for space in range(upper-i): 
       print(' ',end=' ')
    # inner loop for jth columns
    for j in range(1, 2*i):
        print('B ',end="")

    print()
# Lower triangle shape    
lower = 4
for i in range (lower,0,-1):
    print(' ',end=' ')
    for space in range(lower-i):
        print(' ',end=' ')
    # inner loop for jth columns
    for j in range(1, 2*i):
        print('B ',end="")
    print()
    
    
    
#         B
#       B B B
#     B B B B B
#   B B B B B B B
# B B B B B B B B B
#   B B B B B B B
#     B B B B B
#       B B B
#         B




# outer loop for ith rows
for i in range (70,65,-1):
    # inner loop for jth columns
    for j in range(65,i):
        print(chr(j),end="")
        
    print()
    
    
# ABCDE
# ABCD
# ABC
# AB
# A




# outer loop for ith rows
for i in range (65,70):
    # inner loop for jth columns
    for j in range(65,70):
        print(chr(i),end="")
        
    print()
    
    
    
# AAAAA
# BBBBB
# CCCCC
# DDDDD
# EEEEE




# outer loop for ith rows
for i in range (ord('P'),ord('U')+1):
    # inner loop for jth columns
    for j in range(ord('P'),i+1):
        print(chr(j),end="")
        
    print()
    
# P
# PQ
# PQR
# PQRS
# PQRST
# PQRSTU




# outer loop for ith rows
for i in range (ord('P'),ord('U')+1):
    # inner loop for jth columns
    for j in range(ord('P'),i+1):
        print(chr(j),end="")
        
    print()
    
    
#        ABCDE
#        ABCD
#         ABC
#          AB
#           A




rows=7
# outer loop for ith rows

for i in range (1,rows+1):
    for space in range(rows-i): 
       print(' ',end=' ')
    # inner loop for jth columns
    for j in range(1, 2*i):
        print('o ',end="")

    print()
    
    
#             o 
#           o o o 
#         o o o o o 
#       o o o o o o o 
#     o o o o o o o o o 
#   o o o o o o o o o o o 
# o o o o o o o o o o o o o 





# alphabetic square alphabet pattern
size = 5
count = 0

for i in range(size):
    for j in range(size):
        print(chr(65 + count), end=" ")
        count += 1
    print()
# A B C D E 
# F G H I J 
# K L M N O 
# P Q R S T 
# U V W X Y





# diamond alphabet pattern program
n = 3

# Upper triangle shape
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print(chr(65 + j), end='')
    print()

# Lower triangle shape 
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print(chr(65 + j), end='')
    print()
#   A
#  ABC
# ABCDE
#  ABC
#   A



str= "PRISKA" 
# Outer loop
for i in range(0,7):
    # inner loop
    for j in range(0,i+1):
        print(str[j],end="")
    print()
    
    
# P
# PR
# PRI
# PRIS
# PRISK
# PRISKA




# Outer loop
for i in range(65,71):
    # Inner loop
    for j in range(i,64,-1):
        print(chr(j),end="")
    print()
# A
# BA
# CBA
# DCBA
# EDCBA
# FEDCBA




rows=5
# outer loop for ith rows
for i in range (rows,0,-1):
    for space in range(rows-i):
        print(' ',end=' ')
        
    # inner loop for jth columns
    for j in range(1, 2*i):
        print('D ',end="")
    print()
# D D D D D D D D D 
#   D D D D D D D 
#     D D D D D 
#       D D D 
#         D 




row = 7
for i in range(1, row+1):
    count = 0
    for j in range(i):
        if j == 0 or j == i-1:
            print(chr(65 + count), end='')
            count += 1
            
        else:
            if i != row:
                print(' ', end='')
            else:
                print(chr(65 + count), end='')
                count += 1
    print()
# A
# AB
# A B
# A  B
# A   B
# A    B
# ABCDEFG




# hourglass alphabet pattern
row = 5

# Lower triangle shape    
for i in range(row-1):
    for j in range(i):
        print(' ', end='')
    for k in range(2*(row-i)-1):
        print(chr(65 + k), end='')
    print()

# Upper triangle shape
for i in range(row):
    for j in range(row-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print(chr(65 + k), end='')
    print()
# ABCDEFGHI
#  ABCDEFG
#   ABCDE
#    ABC
#     A
#    ABC
#   ABCDE
# ABCDEFG
# ABCDEFGHI