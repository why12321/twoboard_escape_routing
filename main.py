import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import a_star
import map


class Env():
    def __init__(self,mp):
        self.mp_k=deepcopy(mp)

map_m=np.load('./data/mp[0].npy')


plt.imshow(map_m)
plt.show()

a_star1 = a_star.AStar(map.mp, 15, 11, 13, 96)
a_star1.RunAndSaveImage()
plt.imshow(map.mp[0])
plt.show()

map.mp[0, 14:17, 10:13] = np.where(map.mp[0, 14:17, 10:13] != 15, 1, map.mp[0, 14:17, 10:13])
map.ObtainObstacle(a_star1.path)

a_star2 = a_star.AStar(map.mp[0], 7, 3, 17, 96)
a_star2.RunAndSaveImage()
plt.imshow(map.mp[0])
plt.show()

map.mp[0, 6:9, 3:5] = np.where(map.mp[0, 6:9, 3:5] != 15, 1, map.mp[0, 6:9, 3:5])
map.ObtainObstacle(a_star2.path)
plt.imshow(map.mp[0])
plt.show()

# map.mp[6:9, 3:4] = 6
# map.mp[6:9, 4:5] = 6

# a_star3 = a_star.AStar(map.mp, 11, 7, 21, 27)
# a_star3.RunAndSaveImage()
# plt.imshow(map.mp)
# plt.show()