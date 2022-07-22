import time
import math

print("Starting")
print(" The equation of interest is: 1-40.775*((3+xl)/(3*xl+((xl**2)/2))**3)=0 ")
xl = float(input("what is initial xl?"))
xu = float(input("what is initial xu?"))
method = int(input("1 for Bisection Method, 2 for False Position Method"))

n=1
xr = xl/2+xu/2
xxr = 0 #placeholder, so the ERR function works correctly

while method == 1:
    
    time.sleep(1)
    xr = xl/2+xu/2
    ERR = abs((xxr-xr)/xr)
    print (ERR)
    fxl = 1-40.775*((3+xl)/(3*xl+((xl**2)/2))**3)
    fxr = 1-40.775*((3+xr)/(3*xr+((xr**2)/2))**3)
    fxrfxl = fxl*fxr
    xxr = xr #store old xr
    
    print("Iteration: ", n, "xl: ", xl, "xu: ", xu, "xr: ", xr, "f(xl): ", fxl, "f(xr) :", fxr, "f(xr)*f(xl): ", fxrfxl, "ERROR: ", ERR)
    
    n = n+1
    
    if fxrfxl < 0:
        xu = xr
        #print("XU: ", xu)
    elif fxrfxl > 0:
        xl = xr
        #print("XL: ", xl)
    elif fxrfxl == 0:
        print("root is:", xr)
    
    
    #ERR = (xu-xr)/xr
    
    if ERR < 0.01:
        print("SUCCESS - ERROR UNDER 1%")
        break
    
while method == 2:
    time.sleep(1)
    fxu = 1-40.775*((3+xu)/(3*xu+((xu**2)/2))**3)
    fxl = 1-40.775*((3+xl)/(3*xl+((xl**2)/2))**3)
    xr = xu-((fxu*(xl-xu))/(fxl-fxu))
    fxr = 1-40.775*((3+xr)/(3*xr+((xr**2)/2))**3)
    fxrfxl = fxl*fxr
    ERR = abs((xxr-xr)/xr)
    #print("LOOK HEREEEEE:  ", xxr, xr) #debug
    xxr = xr#store old xr 
    print("Iteration: ", n, "xl: ", xl, "xu: ", xu, "xr: ", xr, "f(xl): ", fxl, "f(xr) :", fxr, "f(xr)*f(xl): ", fxrfxl, "ERROR: ", ERR)
    if fxrfxl < 0:
        xu = xr
    elif fxrfxl > 0:
        xl = xr
    elif fxrfxl == 0:
        print("root is:", xr)
    
    n = n+1
    if ERR < 0.01:
        print("SUCCESS - ERROR UNDER 1%")
        break
    