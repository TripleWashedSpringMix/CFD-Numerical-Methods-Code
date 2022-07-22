import time

print(" example = 3*x1+4*x2-x3 -> A*x1+B*x2-C*x3")

x11 = float(input("Equation 1 A=?"))
x12 = float(input("Equation 1 B=?"))
x13 = float(input("Equation 1 C=?"))
a1 = float(input("= ?: "))

x21 = float(input("Equation 2 A=?"))
x22 = float(input("Equation 2 B=?"))
x23 = float(input("Equation 2 C=?"))
a2 = float(input("= ?: "))

x31 = float(input("Equation 3 A=?"))
x32 = float(input("Equation 3 B=?"))
x33 = float(input("Equation 3 C=?"))
a3 = float(input("= ?: "))

print("original matrix: ")
print(x11, x12, x13, "|", a1)
print(x21, x22, x23, "|", a2)
print(x31, x32, x33, "|", a3)

time.sleep(1)

A = x21 - x11*(x21/x11)
B = x22 - x12*(x21/x11)
C = x23 - x13*(x21/x11)
a2 = a2 - a1*(x21/x11)

A1 = x31 - x11*(x31/x11)
B1 = x32 - x12*(x31/x11)
C1 = x33 - x13*(x31/x11)
a3 = a3 - a1*(x31/x11)

print("first row pivoting matrix: ")
print(x11, x12, x13, "|", a1)
print(A, B, C, "|", a2)
print(A1, B1, C1, "|", a3)

time.sleep(1)

A1 = A1 - A*(B1/B)
B11 = B1 - B*(B1/B)
C1 = C1 - C*(B1/B)
a3 = a3 - a2*(B1/B)

print("second row pivoting matrix: ")
print(x11, x12, x13, "|", a1)
print(A, B, C, "|", a2)
print(A1, B11, C1, "|", a3)

time.sleep(1)

x3 = a3/C1
x2 = (a2 - C*x3 )/B
x1 = (a1 - x12*x2 - x13*x3)/x11

print("root of the matrix is: ", "x1 = ", x1, "x2 = ", x2, "x3 = ", x3)
