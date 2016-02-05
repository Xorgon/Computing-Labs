import math


def swing_time(L):
    """
    Computes and returns the time needed for an idealized pendulum to complete
    a single oscillation.

    L -- length of pendulum (must be >= 0)

    returns time T seconds
    if L < 0 returns 0
    """
    if L >= 0:
        return 2 * math.pi * math.sqrt(L / 9.81)
    else:
        return 0


def range_squared(n):
    """Computes and returns the squares of the numbers from 0 to n-1."""
    squares = []
    for k in range(n):
        squares.append(k ** 2)
    return squares


def count(element, seq):
    """Counts and returns the number of times element occurs in the sequence"""
    return seq.count(element)
