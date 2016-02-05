import scipy.integrate
import math


def trapez(f, a, b, n):
    """
    Computes and returns a trapezoidal approximate integral of f.

    f -- function
    a -- lower boundary
    b -- upper boundary
    n -- number of sections

    returns approximate integral using the trapezoidal method
    """
    h = (b-a)/float(n)
    sum_fx = 0.0
    for i in range(n-1):
        xi = a + (i+1) * h
        sum_fx += f(xi)
    return h * (f(a) + f(b) + 2.0 * sum_fx) / 2.0


def finderror(n):
    """ Computes and returns the error when using trapez with n values. """
    approx_i = trapez(lambda x: x*x, -1, 2, n)
    exact_i = 3
    return exact_i - approx_i


def using_quad():
    """ Computes and returns the output of scipy quad for x^2 between -1, 2 """
    return scipy.integrate.quad(lambda x: x ** 2, -1, 2)


def std_dev(x):
    """ Computes and returns the corrected sample standard deviation of x. """
    N = len(x)
    mu = sum(x)/N
    sum_sd = 0.0
    for i in range(N):
        sum_sd += (x[i] - mu) ** 2
    return math.sqrt(sum_sd/(N - 1))
