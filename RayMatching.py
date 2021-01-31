import numpy as np
import pygame #pylint: disable=import-error
from Camera import Camera
from Sphere import Sphere

#res = (640, 480)
res = (100, 100)

maxSteps = 10

c = Camera([5, 5], res, [0, 0, 0], 0, 5)

objects = [Sphere([20, 0, 0], 5, pygame.Color(200, 0, 0))]

pygame.init()
screen = pygame.display.set_mode(res)

while True:
    rays, points = c.getRays()
    for x in range(res[0]):
        for y in range(res[1]):
            point = np.copy(points[x][y])

            i = 0
            hit = False
            while not hit:
                i += 1

                if i >= maxSteps:
                    pygame.draw.circle(screen, pygame.Color(0, 0, 0), (x,y), 1)
                    hit = True

                step = min([o.getDistance(point) for o in objects])

                if step <= 0:
                    pygame.draw.circle(screen, pygame.Color(0, 0, 200), (x,y), 1)
                    hit = True

                point += rays[x][y] * step




    pygame.display.flip()
    print("frame")
