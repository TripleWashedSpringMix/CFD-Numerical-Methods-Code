import math
import time

def f(x):
    res = (4.1585*10**-5)*(1296*math.cos(0.5236*x)-1296+279.0565*x**2-31.007*x**3)-0.009
    return res
 
def dfdx(x):
    res = abs(0.00898*math.pi*math.sin((math.pi*x)/6)+0.0001248*((math.pi)**3)*x**2-0.0007485*((math.pi)**3)*x)
    return res

i = 1  # initial iteration
x0 = 1.8  # Initial guess
err = 1 #initial error
xi_1 = x0


print("Iteration: " + str(i) + ": x = " + str(x0) + ", f(x) = " +    
          str(f(x0)) + "f'(x) = " + str(dfdx(x0)) + "ERROR = " + str(err))

# Iterating until either the tolerance or max iterations is met
while err > 0.0001:
    time.sleep(0.1)
    i = i + 1
    xi = xi_1-f(xi_1)/abs(dfdx(xi_1))
    err = abs((xi-xi_1)/xi)
    print("Iteration: " + str(i) + ": x = " + str(xi) + ", f(x) = " +    
          str(f(xi)) + "f'(x) = " + str(dfdx(xi)) + "ERROR = " + str(err))
    #err = abs((xi-xi_1)/xi)
    #print(err)
    xi_1 = xi
    