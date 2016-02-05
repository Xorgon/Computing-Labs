import math
import pylab
import scipy.optimize
plot = pylab.plot
legend = pylab.legend


def f1(x):
    """ Computes and returns f1(x). """
    return math.cos(2.0 * x * math.pi) * math.exp(- x ** 2)


def f2(x):
    """ Computes and returns f2(x). """
    return math.log(x + 2.2)


def f3(x):
    """ Computes and returns f1(x) - f2(x). """
    return f1(x) - f2(x)


def create_plot_data(f, xmin, xmax, n):
    """
    Computes and returns values of y = f(x).

    f -- function of x
    xmin -- minimum value of x
    xmax -- maximum value of x
    n -- number of values of x

    returns values of x and y
    """
    xs = []
    ys = []
    for i in range(n):
        xi = xmin + float(i) * (xmax - xmin) / (n - 1)
        yi = f(xi)
        xs.append(xi)
        ys.append(yi)
    return (xs, ys)


def myplot():
    """ Plots f1 and f2, displays graph, saves pdf and png, returns None. """
    data1 = create_plot_data(f1, -2, 2, 1001)
    data2 = create_plot_data(f2, -2, 2, 1001)
    plot(data1[0], data1[1], label="f1")
    plot(data2[0], data2[1], label="f2")
    pylab.xlabel("x")
    legend()
    pylab.savefig("plot.png")
    pylab.savefig("plot.pdf")
    return None


def find_cross():
    """ Computes and returns an approximate root of f1(x) - f2(x) = 0 """
    return scipy.optimize.brentq(f3, 0.091, 0.093)
