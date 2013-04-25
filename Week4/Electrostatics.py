import numpy as np
def pointPotential(x,y,q,posx,posy):
    k = 1.04e-23
    q=1e-19 #define k and q
    
    Vxy = (k*q/((x-posx)**2 + (y - posy)**2))**(1/2.) #replace the d with posx and posy; only use first term in dipole equation
    return Vxy

def dipolePotential(x,y,q,d):
    k = 1.04e-23
    q=1e-19
    V = (k*q/(x**2 + (y - d/2)**2)**(1/2.)) - (k*q/(x**2 + (y+d/2)**2)**(1/2.))
