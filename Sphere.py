import numpy as np

class Sphere():
    def __init__(self, pos, radius, color):
        self.pos = np.array(pos)
        self.radius = radius
        self.color = color

    def getDistance(self, point):
        point = np.array(point)
        dis = np.linalg.norm(point - self.pos) - self.radius
        return dis
