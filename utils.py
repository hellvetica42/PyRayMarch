import numpy as np

def rotateZ(vector, angle):
    theta = np.radians(angle)
    s, c = np.sin(theta), np.cos(theta)
    R = np.array(((c, -s, 0),
                 (s, c, 0),
                 (0, 0, 1)))

    return R.dot(vector)
    

