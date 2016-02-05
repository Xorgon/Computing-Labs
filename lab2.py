
def seconds2days(seconds):
    """Accepts a value in seconds and returns its value in days."""
    return seconds/(60.0*60.0*24.0)


def box_surface(a, b, c):
    """
    Computes the surface area of a cuboid.

    a,b,c -- Edge lengths of the cuboid.

    returns surface area
    """
    return 2.0 * (a * b + b * c + c * a)


def triangle_area(a, b, c):
    """
    Computes the area of a triangle.

    a,b,c -- Side lengths of the triangle.

    returns area
    returns 0 if sides are invalid.
    """
    s = (a + b + c)/2.0
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared < 0:
        return 0
    else:
        return area_squared ** 0.5
