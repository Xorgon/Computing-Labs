import numpy as np
from scipy import optimize


def model(t, Ti, Ta, c):
    """ Computes and returns the model function for lab 10. """
    return (Ti - Ta) * np.exp(- t / c) + Ta


def read2coldata(filename):
    """ Returns a tuple containing the columns in input document. """
    f = open(filename, 'r')
    lines = f.readlines()
    print(lines)
    col1 = []
    col2 = []
    for line in lines:
        sp = line.split()
        col1.append(float(sp[0]))
        col2.append(float(sp[1]))
    return (np.array(col1), np.array(col2))


def extract_parameters(ts, Ts):
    """ Extracts and returns the parameters for the model function. """
    out = optimize.curve_fit(model, ts, Ts, p0=[85.0, 20.0, 600])
    Ti = out[0][0]
    Ta = out[0][1]
    c = out[0][2]
    return Ti, Ta, c


def sixty_degree_time(Ti, Ta, c):
    """ Estimates and returns the number of seconds until drinkable. """
    return optimize.newton(lambda t, Ti, Ta, c: model(t, Ti, Ta, c) - 60,
                           288, args=(Ti, Ta, c))
