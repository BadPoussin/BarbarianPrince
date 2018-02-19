import math


class Point:
    def __init__(self, x=67, y=65):
        self.x = x
        self.y = y


class Cube:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


def create_grid():
    listPoints = []
    size = 23
    center = Point()

    for y in range(0, 6):
        for x in range(0, 6):
            cube = oddq_to_cube(x, y)
            point = cube_to_axial(cube)
            newCenter = Point(int(center.x + point.x), int(center.y + point.y))
            listPoints.append(create_list(newCenter, size))

    return listPoints


def hex_to_pixel(q, r, size):
    y = size * math.sqrt(3) * (r + q / 2)
    x = size * 3 / 2 * q
    return Point(x, y)


def oddq_to_cube(q, r):
    x = q
    z = r - (q - q & 1) / 2
    y = -x - z
    cube = Cube(x, y, z)
    return cube


def cube_to_axial(cube):
    q = cube.x
    r = cube.z
    point = Point(q, r)
    return point


def cube_to_oddq(cube):
    col = cube.x
    row = cube.z + (cube.x - (cube.x & 1)) / 2
    return Point(col, row)


def create_list(center, size):
    listPoints = []
    for i in range(1, 7):
        listPoints.append(hex_corner(center, size, i))
    return listPoints


def hex_corner(center, size, i):
    angle_deg = 60 * i
    angle_rad = math.pi / 180 * angle_deg
    return center.x + size * math.cos(angle_rad), center.y + size * math.sin(angle_rad)
