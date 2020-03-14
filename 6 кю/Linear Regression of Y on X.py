def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    x2 = [float(i**2) for i in x]
    y2 = [float(i**2) for i in y]
    xy = [x[i]*y[i] for i in xrange(0,len(x))]
    a = (sum(x2)*sum(y) - sum(x)*sum(xy))/(len(x)*sum(x2) - sum(x)**2)
    b = (len(x)*sum(xy) - sum(x)*sum(y))/(len(x)*sum(x2) - sum(x)**2)
    return (round(a,4),round(b,4))
