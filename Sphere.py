import numpy as np

class Sphere():
    def __init__(self, pos, radius, color):
        self.pos = np.array(pos)
        self.radius = radius
        self.color = color

    def getDistances(self, points):
        #Array of points of position of object
        P = np.full((points.shape), self.pos)

        #Euclidian distance
        diff_vectors = P - points 
        diff_vectors = diff_vectors**2

        #Sum of each point's squared elements. now 2D array
        sums = np.sum(diff_vectors, axis=2)

        #Euclidian distance for each point
        distances = np.sqrt(sums)
        
        #Spheres are simple
        distances -= self.radius

        return distances
