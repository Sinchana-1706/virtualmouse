import math

def get_distance(points):
    """
    Calculates the Euclidean distance between two landmarks.
    :param points: List of two (x, y) tuples [(x1, y1), (x2, y2)]
    :return: Distance in pixels (float)
    """
    if len(points) != 2:
        raise ValueError("get_distance requires exactly two points")
    (x1, y1), (x2, y2) = points
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 1000  # scaled for better detection


def get_angle(a, b, c):
    """
    Calculates the angle (in degrees) formed at point 'b' by points a, b, and c.
    :param a: (x, y) of first point
    :param b: (x, y) of middle point (vertex)
    :param c: (x, y) of third point
    :return: Angle in degrees (float)
    """
    # Vectors BA and BC
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])

    # Dot product and magnitudes
    dot_product = ba[0] * bc[0] + ba[1] * bc[1]
    mag_ba = math.sqrt(ba[0] ** 2 + ba[1] ** 2)
    mag_bc = math.sqrt(bc[0] ** 2 + bc[1] ** 2)

    if mag_ba == 0 or mag_bc == 0:
        return 0.0

    # Calculate angle in degrees
    cos_angle = dot_product / (mag_ba * mag_bc)
    cos_angle = max(-1, min(1, cos_angle))  # clamp to valid range
    angle = math.degrees(math.acos(cos_angle))
    return angle

