# ---------------------------------------------------------------------------
# Integral assignement
# Contains a self written integrate algorithm that can integrate any function
# There are different algorithm implemented, one time with the weighted mean value,
# the simpson algorigthm and the modified simpson algorightm for singularity functions
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

import numpy
from scipy.integrate import quad
import math

# Integrates a given function within the given range.
# Steps can be optionaly defined.
def Integrate(f, min, max, steps = 20):
    result = 0
    for x in range(0, steps):
        currentPos = math.fabs(min - max) / steps * x  # a
        nextPos = math.fabs(min - max) / steps * (x+1) # b
        width = math.fabs(currentPos - nextPos)        # | a - b |
        height = (f(currentPos) + f(nextPos)) / 2      # (f(a) + f(b)) / 2
        
        result += height * width
    return result

# Integrates the given function using the Simpson Algorithm
# (Weighted values at a, b, and mean value)
def IntegrateSimpsons(f, min, max, steps = 20):
    result = 0
    for x in range(0, steps):
        currentPos = math.fabs(min - max) / steps * x   # a
        nextPos = math.fabs(min - max) / steps * (x+1)  # b
        width = math.fabs(currentPos - nextPos)         # | a - b |
              
        result += 1/3 * (width) / 2 * f(currentPos) + 4/3 * (width)/2 * f((currentPos+nextPos)/2) + 1/3*(width)/2*f(nextPos)
    return result

def f(x):
    return numpy.log(math.sin(x))

# Integrates the given function using the Simpson Algorithm
# (Weighted values at a, b, and mean value)
def IntegralModifiedSimpson(f,A,B,N):
    la=[]
    lb=[]    
    for n in range(0,N):
        a=A+((B-A)/N)*n
        la.append(a)
        
        b=a+((B-A)/N)
        lb.append(b)
                
    i=0
    z=0
    while i<N:
        z+=3/2*((lb[i]-la[i])/6*f((la[i]+lb[i])/2))+9/4*(((lb[i]-la[i])/6*f((la[i]+lb[i])/2-(lb[i]-la[i])/3))+((lb[i]-la[i])/6*f((la[i]+lb[i])/2+(lb[i]-la[i])/3)))
        i+=1
    return z

def TestIntegrateFunction():

    print("Normal value")
    # Test cos integration
    print("cos(x) from 0 to 2:")
    print("Numeric solution: %f" % (Integrate(math.cos, 0, 2)))
    print("Correct value: %f" % (math.sin(2)))
    print("Error: %f" % (math.sin(2)-Integrate(math.cos, 0, 2)))
    print()
    # Test e^x function
    print("e**x from 0 to 10")
    print("Numeric solution: %f" % (Integrate((lambda x: math.e**x), 0, 10)))
    print("Correct value: %f" % (math.e**10 - math.e**0))
    print("Error: %f" % (math.e**10 - math.e**0  -Integrate((lambda x: math.e**x), 0, 10)))

def TestIntegrateSimpsonFunction():
    print("Simpson method")
    # Test cos integration$
    print("cos(x) from 0 to 2:")
    print("Numeric solution: %f" % (IntegrateSimpsons(math.cos, 0, 2)))
    print("Correct value: %f" % (math.sin(2)))
    print("Error: %f" % (math.sin(2)-IntegrateSimpsons(math.cos, 0, 2)))
    print()
    # Test e^x function
    print("e**x from 0 to 10")
    print("Numeric solution: %f" % (IntegrateSimpsons((lambda x: math.e**x), 0, 10)))
    print("Correct value: %f" % (math.e**10 - math.e**0))
    print("Error: %f" % (math.e**10 - math.e**0  -IntegrateSimpsons((lambda x: math.e**x), 0, 10)))

TestIntegrateFunction()
print()
print()
TestIntegrateSimpsonFunction()
print()
print("Test modified simpson function")
print(IntegralModifiedSimpson(f,0,math.pi/2,500))
print(quad(f,0,math.pi/2))