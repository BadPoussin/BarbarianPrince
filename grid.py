import math

size = 19.5


class Point:
    def __init__(self, x=76.5, y=97):
        self.x = x
        self.y = y


def create_grid():
    listPoints = []
    center = Point()

    for y in range(0, 23):
        for x in range(0, 20):
            point = oddq_offset_to_pixel(x, y, size)
            newCenter = Point(int(center.x + point.x), int(center.y + point.y))
            listPoints.append(create_list(newCenter, size))

    return listPoints


def update_grid(posX, posY):
    listPoints = []
    hexToColored = []
    hexCliqued = -1
    center = Point()
    hexCenter = Point()

    for y in range(0, 23):
        for x in range(0, 20):
            point = oddq_offset_to_pixel(x, y, size)
            newCenter = Point(int(center.x + point.x), int(center.y + point.y))
            listPoints.append(create_list(newCenter, size))
            if math.sqrt(math.pow(newCenter.x - posX, 2) + math.pow(newCenter.y - posY, 2)) < size:
                hexCliqued = len(listPoints) - 1
                hexCenter = newCenter
                if x == 0:
                    hexToColored = [len(listPoints), len(listPoints) - 20,
                                    hexCliqued - 20, hexCliqued + 20]
                elif x == 19:
                    hexToColored = [len(listPoints) - 2, len(listPoints) + 18,
                                    hexCliqued - 20, hexCliqued + 20]
                elif x % 2 != 0:
                    hexToColored = [len(listPoints) - 2, len(listPoints), len(listPoints) + 18, len(listPoints) + 20,
                                    hexCliqued - 20, hexCliqued + 20]
                else:
                    hexToColored = [len(listPoints) - 2, len(listPoints), len(listPoints) - 22, len(listPoints) - 20,
                                    hexCliqued - 20, hexCliqued + 20]

    return listPoints, hexCliqued, hexCenter, hexToColored


def search_hexagon(pos):
    return update_grid(pos[0], pos[1])


def oddq_offset_to_pixel(q, r, size):
    x = size * 3 / 2 * q
    y = size * math.sqrt(3) * (r + 0.5 * (q & 1))
    return Point(x, y)


def create_list(center, size):
    listPoints = []
    for i in range(1, 7):
        listPoints.append(hex_corner(center, size, i))
    return listPoints


def hex_corner(center, size, i):
    angle_deg = 60 * i
    angle_rad = math.pi / 180 * angle_deg
    return center.x + size * math.cos(angle_rad), center.y + size * math.sin(angle_rad)
