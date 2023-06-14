import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import a_star
import map


class Env():
    def __init__(self,mp):
        self.mp_k=deepcopy(mp)

map_m=np.load('./data/mp.npy')


plt.imshow(map_m)
plt.show()

a_star1 = a_star.AStar(map.mp, 15, 11, 13, 27)
a_star1.RunAndSaveImage()
plt.imshow(map.mp)
plt.show()
