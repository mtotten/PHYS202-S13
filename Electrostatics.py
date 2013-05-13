import numpy as np
def pointPotential(x,y,q,posx,posy):
    k = 1.04e-23
    q=1e-19 #define k and q

    Vxy = (k*q/((X-posx)**2 + (Y - posy)**2))**(1/2.) #replace the d with posx $
    return Vxy



def dipolePotential(x,y,q,d):
    k = 1.04e-23
    q=1e-19
    V = (k*q/(X**2 + (Y - d/2)**2)**(1/2.)) - (k*q/(X**2 + (Y+d/2)**2)**(1/2.))$

    Vxy = V #sum up the functions
    return Vxy

def pointField(x,y,q,Xq,Yq):
    k = 1.04e-23
    q = 1e-19
    Ex = k*q*(x-Xq)/(((x-Xq)**2+(y-Yq)**2)**.5)
    Ey = k*q*(y-Yq)/(((x-Xq)**2+(y-Yq)**2)**.5)
    return Ex,Ey

