import numpy as np

def finiteDifference(x,y):
    """takes x and y inputs and computes the derivative"""
    dydx = np.zeros(y.shape,float)
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2])
    dydx[-1] = (y[-1]-y[-2])/(x[-1-x[-2])
    return dydx

def fourPtFiniteDiff(x,y):
    """takes x and y and computes the derivative with the four point method"""
    dydx = np.zeros(y.shape,float)
    dydx[2:-2] = (y[0:-4]-(8*y[1:-3])+(8*y[3:-1]-y[4:])/(12*(x[3]-x[2]))
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    return dydx
