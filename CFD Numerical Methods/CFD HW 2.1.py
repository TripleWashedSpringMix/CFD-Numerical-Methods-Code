from __future__ import division
import time
import math
from operator import itemgetter

#import numpy

Re1 = 174981
Re2 = 94682
Re3 = 80281
Re4 = 43955
Re5 = 36309
Re6 = 21680
Re7 = 14628
Re8 = 36309
Re9 = 80281
n = 0 #probs needs to be inside the loop smh
pn = 1 #pipe number
nn = 1 #iteration counter
#u = #probs needs to be inside the loop smh
#l = #probs needs to be inside the loop smh


a = [Re1, Re2, Re3, Re4, Re5, Re6, Re7, Re8, Re9, 0] # array
L = [2,4,2,4,2,4,8,2,2]

method = int(input("1 for Secant Method, 2 for False Position Method"))

if method == 1:
    x0 = float(input("what is initial xi-1?"))
    x1 = float(input("what is initial xi?"))
    xx0 = x0
    xx1 = x1
if method == 2:
    xl = float(input("what is initial xl?"))
    xu = float(input("what is initial xu?"))
    xxl = xl
    xxu = xu
    xxr = 0 #placeholder, so the ERR function works correctly


#fof = 4*math.log(Re*f^0.5,10)-f^-.5-0.4 #refference, nstbh
#dfof = 2*(math.ln(10)*f+2x^-1.5) #derrivative of fof, nstbh
#fu = 4*math.log(Re*u^0.5,10)-u^-.5-0.4


#dif = x0-x1

#fr = fu - (fu*(dif))/(fx0-fx1)

while method == 1: #SECANT
    a = [Re1, Re2, Re3, Re4, Re5, Re6, Re7, Re8, Re9]
    time.sleep(0.1)
    ind_pos = [n] # indexing the positon of a value in the array
    Re = itemgetter(*ind_pos)(a) #get the needed value
    print (Re) #debug for my sanity
    
    time.sleep(0.1)
    fx0 = float(4*math.log(Re*x0**0.5,10)-x0**-.5-0.4)
    #print(fx0)
    fx1 = float(4*math.log(Re*x1**0.5,10)-x1**-.5-0.4)
    err = (x1-x0)/x1
    
   
    x2 = x1 - ((float(fx1)*(float(x0)-float(x1)))/((float(fx0)-float(x1))))
    
    err = abs((x1-x0)/x1)
    
    print("Iteration: ", nn, "xi-1: ", x0, "xi: ", x1, "xi+1: ", x2, "f(xi): ", fx1, "f(xi-1) :", fx0, "ERROR: ", err)
    nn = nn +1
    
    x0 = x1
    x1 = x2

    if err < 0.005:
        
        print("SUCCESS, PIPE", pn, "- ERROR UNDER 1%")
        pn=pn+1
        n=n+1
        x0 = xx0
        x1 = xx1
    elif pn == 9 or n == 9:
        print("DONE")
        break

while method == 2: #FALSE POSITION
    a = [Re1, Re2, Re3, Re4, Re5, Re6, Re7, Re8, Re9, 0]
    time.sleep(0.1)
    ind_pos = [n] # indexing the positon of a value in the array
    Re = itemgetter(*ind_pos)(a) #get the needed value
    print (Re) #debug for my sanity
    fxu = 4*math.log(Re*xu**0.5,10)-xu**-.5-0.4
    fxl = 4*math.log(Re*xl**0.5,10)-xl**-.5-0.4
    xr = xu-((fxu*(xl-xu))/(fxl-fxu))
    fxr = 4*math.log(Re*xr**0.5,10)-xr**-.5-0.4
    fxrfxl = fxl*fxr
    ERR = abs((xxr-xr)/xr)
    xxr=xr
    if fxrfxl < 0:
        xu = xr
        #print("XU: ", xu)
    elif fxrfxl > 0:
        xl = xr
        #print("XL: ", xl)

    elif fxrfxl == 0:
        print("root is:", xr)
    
   
    print("Iteration: ", nn, "xl: ", xl, "xu: ", xu, "xr: ", xr, "f(xl): ", fxl, "f(xr) :", fxr, "f(xr)*f(xl): ", fxrfxl, "ERROR: ", ERR)
    nn = nn +1
    if ERR < 0.005:
        
        print("SUCCESS, PIPE", pn, "- ERROR UNDER 1%")
        pn=pn+1
        n=n+1
        xl = xxl
        xu = xxu
        lol = input("press anything to continue on your wild ride")
    elif pn == 10 or n == 10:
        print("DONE")
        break
