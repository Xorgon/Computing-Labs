def vector_product3(a, b):
    """Computes and returns the vector product of vectors a and b."""
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def seq_mult_scalar(a, s):
    """Returns a list of the products of s with the values in list a."""
    prod_as = []
    for n in a:
        prod_as.append(n*s)
    return prod_as


def powers(n, k):
    """Computes and returns a list of n to the powers 0 through k."""
    n_pows = []
    for i in range(k+1):
        n_pows.append(n**i)
    return n_pows


def traffic_light(load):
    """Returns green, amber or red depending on the value of load."""
    if load < 0.7:
        return "green"
    elif load < 0.9:
        return "amber"
    else:
        return "red"
