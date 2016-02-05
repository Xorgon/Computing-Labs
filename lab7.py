def derivative(f, x, eps=1e-6):
    """
    Computes a numerical approximation of the first derivative of a function.

    f -- Function to find the first derivative of
    x -- The value to calculate the first derivative for
    eps -- The value of epsilon in the equation, default = 1e-6

    returns approximation of the first derivative of the function
    """
    return (f(x + eps/2) - f(x - eps/2))/eps


def newton(f, x, feps, maxit):
    """
    Computes a Newton-Raphson method approximation of a root of function f

    f -- Function to find the root of
    x -- Initial guess as to the value of the root
    feps -- Allowable tolerance of error for the root
    maxit -- Maximum iterations of the method

    returns approximation of the root

    throws RuntimeError
    """
    k = 0
    while (abs(f(x)) > feps) and (k < maxit):
        k += 1
        x = x - f(x) / derivative(f, x)
    if (k < maxit):
        return x
    else:
        raise RuntimeError("Failed after %d iterations" % maxit)


def is_palindrome(s):
    """Returns boolean test of whether s is a palindrome."""
    for i in range(len(s)):
        if s[i] == s[len(s) - 1 - i]:
            continue
        else:
            return False
    return True
