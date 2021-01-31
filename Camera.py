import numpy as np
from utils import rotateZ

class Camera():
    def __init__(self, size, resolution, pos, direction, focal_distance):
        self.size = size
        self.resolution = resolution
        self.pos = pos
        self.direction = direction #Angle around z axis only. To be axpanded
        self.focal_distance = focal_distance
        pass

    def getRays(self):
        plane = np.zeros((self.resolution[0], self.resolution[1], 3))
        rays = np.zeros((self.resolution[0], self.resolution[1], 3))


        xvals = np.linspace(-(self.size[0]/2), (self.size[0]/2), self.resolution[0])
        xmatrix = np.tile(xvals, (self.resolution[1], 1))
        #y values are all 0
        zvals = np.linspace(-(self.size[1]/2), (self.size[1]/2), self.resolution[1])
        zmatrix = np.tile(zvals, (self.resolution[0], 1))

        plane[:, :, 0] = xmatrix.T
        plane[:, :, 2] = zmatrix


        #Rotate all vectors towards direction
        for x in range(len(plane)):
            for y in range(len(plane[x])):
                plane[x][y] = rotateZ(plane[x][y], self.direction-90) #Defalut is looking towards positive X
                #Get unit vectors as rays

        #Translate plane a focal distance away from position
        direction_vec = rotateZ([1, 0, 0], self.direction) #Defalut is looking towards positive X
        plane = plane + (direction_vec * self.focal_distance)

        for x in range(len(plane)):
            for y in range(len(plane[x])):
                rays[x][y] = plane[x][y] / np.linalg.norm(plane[x][y]) 


        return rays, plane 

        



    

                


