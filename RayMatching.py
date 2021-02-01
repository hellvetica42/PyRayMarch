import numpy as np
import pygame #pylint: disable=import-error
from Camera import Camera
from Sphere import Sphere


#res = (640, 480)
res = (100, 100)

maxSteps = 30

c = Camera([5, 5], res, [0, 0, 0], 0, 5)

objects = [Sphere([20, 0, 0], 5, pygame.Color(200, 0, 0))]

pygame.init()
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
rays, points = c.getRays()

while True:

    #For one object only
    sphere = objects[0] 

    tmpPoints = np.copy(points)
    mask = np.full((res), False)
    for i in range(maxSteps):

        distances = sphere.getDistances(tmpPoints)
        tmpRays = np.copy(rays)

        tmpRays[:, :, 0] *= distances
        tmpRays[:, :, 1] *= distances
        tmpRays[:, :, 2] *= distances

        tmpPoints = tmpPoints + tmpRays 

        #Its that simple ?!?
        newMask = distances <= 0
        #Keeps track of the rays that hit the sphere
        mask = np.logical_or(newMask, mask)


    #mask[mask == True] = [200, 0, 0]
    surfaceArray = np.zeros(points.shape)

    for x in range(res[0]):
        for y in range(res[1]):
            if mask[x][y]:
                surfaceArray[x][y] = [200, 0, 0]

    surface = pygame.surfarray.make_surface(surfaceArray)
    screen.blit(surface, (0,0))


    pygame.display.flip()
    print("frame")
    clock.tick(60)
