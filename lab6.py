def eval_f(f, xs):
    """Takes a list xs and returns values of function f for each value in xs"""
    fs = []
    for x in xs:
        fs.append(f(x))
    return fs


def sum_f(f, xs):
    """Returns sum of values of function f for each value in list xs"""
    sum_f = 0
    for x in xs:
        sum_f += f(x)
    return sum_f


def box_volume_UPS(a=13, b=11, c=2):
    """
    Computes the volume of a UPS box

    a,b,c -- Lengths of sides of box, in inches, by default: 13,11,2

    returns volume of box in inches^3

    """
    return a * b * c
