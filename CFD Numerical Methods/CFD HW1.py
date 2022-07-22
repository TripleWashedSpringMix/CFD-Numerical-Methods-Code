import time

print("Starting")
print(" The equation of interest is: -0.5x*x+2.5*x+4.5")
xl = int(input("what is initial xl?"))
xu = int(input("what is initial xu?"))
#print("DEBUG", xl_in,xu_in) #debug

n=1


while True:
    time.sleep(1)
    xr = xl/2+xu/2
    fxl = -0.5*(xl**2)+2.5*(xl)+4.5
    fxr = -0.5*(xr**2)+2.5*(xr)+4.5
    fxrfxl = fxl*fxr
    ERR = (xu-xr)/xr
    if fxrfxl < 0:
        xu = xr
        #print("XU: ", xu)
    elif fxrfxl > 0:
        xl = xr
        #print("XL: ", xl)

    elif fxrfxl == 0:
        print("root is:", xr)
    
   
    print("Iteration: ", n, "xl: ", xl, "xu: ", xu, "xr: ", xr, "f(xl): ", fxl, "f(xr) :", fxr, "f(xr)*f(xl): ", fxrfxl, "ERROR: ", ERR)
    n = n+1
    if ERR < 0.05:
        print("CONGRATS - ERROR UNDER 5%, MY TIME TO GO TO SLEEP")
        break
    