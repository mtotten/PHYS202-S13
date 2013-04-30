import numpy as np

def pointPotential(x,y,q,posx,posy):
    k = 1.04e-23
    Vxy = (k*q/((x-posx)**2 + (y - posy)**2))**(1/2.) 
    return Vxy

def dipolePotential(x,y,q,d):
    k = 1.04e-23
    V = (k*q/(x**2 + (y - d/2)**2)**(1/2.)) - (k*q/(x**2 + (y+d/2)**2)**(1/2.))
    Vxy = V
    return Vxy
