import numpy as np
from scipy import integrate, optimize, interpolate
import math


def f(x):
    """ Computes and returns function f. """
    return (np.exp(- x ** 2) / (1 + x ** 2) +
            (2 * np.cos(x) ** 2) / (1 + (x - 4) ** 2))


def integrate_f_from0(b):
    """ Computes and returns the approximate integral of f between 0 and b. """
    return integrate.quad(f, 0, b)


def find_max_f():
    """ Computes and returns a maximum value for function f. """
    return optimize.fmin(lambda x: -f(x), 0)


def find_f_equals_1():
    """ Computes and returns an approximate x value when f(x) = 1. """
    return optimize.newton(lambda x: f(x) - 1, 0)


def lin_int(xs, ys):
    """ Returns a linear interpolation function of xs,ys. """
    return interpolate.interp1d(xs, ys, 'linear')


def make_oscillator(frequency):
    """ Returns a function of an oscillator. """
    def f(t):
        return math.sin(t * frequency)
    return f
