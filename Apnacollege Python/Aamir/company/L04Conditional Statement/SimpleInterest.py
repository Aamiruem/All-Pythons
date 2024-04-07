# p = float(input("p : "))
# r = float(input("r : "))
# t = float(input("t : "))
#
# si = (p * t * r) / 100
# print("si : ", si)
#
# ci = p * (1 + r / 100) ** t
# print("ci : ", ci)
#
# f = ci - p * (1 + r / 100) ** t
# print("f : ", f)
#
# print("--------------------------------------")
#
# print("si : ", round(si, 2))
# print("ci : ", round(ci, 2))


# simple interest
p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))

si = (p * t * r) / 100
print("simple interest is : ", si)


# compound interest
p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))

ci = p * (1 + r / 100) ** t

print("compound interest is : ", ci)