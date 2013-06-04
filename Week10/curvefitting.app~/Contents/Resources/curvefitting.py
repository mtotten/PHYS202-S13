def LinearLeastSquaresFit(x,y):
    """Takes in arrays representing (x,y) values for a set of linearly varying data and performs a linear least squares regression. Returns resulting slope and intercept parameters of the best fit line with uncertainties"""
    n = double(len(x))
    xavg = np.mean(x)
    yavg = np.mean(y)
    xsquare = np.mean(x ** 2)
    xy = np.mean(x * y)
    m = (xy - (xavg * yavg)) / (xsquare - (xavg**2))
    b = ((xsquare * yavg) - (xavg * xy))/(xsquare - xavg**2)
    usquare = np.mean((y - (m*x + b))**2)
    uncm = (1/(n-2) * (usquare / (xsquare - xavg**2)))**.5
    uncb = (1/(n-2) * (usquare * xsquare)/(xsquare - xavg**2))**.5                       
    return m, b, uncm, uncb
