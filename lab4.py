def seq_sqrt(xs):
    """Computes and returns a list of the square-roots of each value in xs."""
    sqrts = []
    for n in xs:
        if n >= 0:
            sqrts.append(n ** 0.5)
        else:
            sqrts.append(0)
    return sqrts


def mean(xs):
    """Computes and returns the arithmetic mean of the numbers in xs."""
    sum_xs = 0.0
    for n in xs:
        sum_xs += n
    return sum_xs/len(xs)


def wc(filename):
    """Counts and returns the number of words in the specified file."""
    f = open(filename, 'r')
    lines = f.readlines()
    words = []
    for line in lines:
        words += line.split(" ")
    for i in range(words.count("\n")):
        words.remove("\n")
    return len(words)
