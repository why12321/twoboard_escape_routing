import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import a_star
import map
import time


class Env():
    def __init__(self,mp):
        self.mp_k=deepcopy(mp)

plt.imshow(map.mp[1])
plt.show()
plt.imshow(map.mp[0])
plt.show()

start_time = time.time()
for i in range(len(map.start_point)):

    # 设置net_i的surface的起点和base的终点为4
    map.mp[1, map.start_point[i][0], map.start_point[i][1]] = 4
    map.mp[0, map.end_point[i][0], map.end_point[i][1]] = 4

    # 设置net_i的surface的起点和base的终点可布线
    map.set_start_end_point_routable(1, map.start_point[i][0], map.start_point[i][1])
    map.set_start_end_point_routable(0, map.end_point[i][0], map.end_point[i][1])
    # plt.imshow(map.mp[1])
    # plt.show()
    # plt.imshow(map.mp[0])
    # plt.show()

    # A*布线
    a_star1_1 = a_star.AStar(1, map.start_point[i][0], map.start_point[i][1], map.end_point[i][0], map.end_point[i][1])
    a_star1_1.RunAndSaveImage()
    # map.mp[1, map.start_point[i][0] - 1:map.start_point[i][0] + 2,map.start_point[i][1] - 1:map.start_point[i][1] + 2] = \
    #     np.where(map.mp[1, map.start_point[i][0] - 1:map.start_point[i][0] + 2,map.start_point[i][1] - 1:map.start_point[i][1] + 2] != 15, 1, 15)
    map.ObtainObstacle(a_star1_1.path, 1)

    if a_star1_1.need_via == 1:
        a_star1_0 = a_star.AStar(0, map.start_point[i][0], map.start_point[i][1], map.end_point[i][0], map.end_point[i][1])
        a_star1_0.RunAndSaveImage()
        # map.ObtainObstacle(a_star1_0.path)
        # map.mp[0, map.end_point[i][0] - 1:map.end_point[i][0] + 2, map.end_point[i][1] - 1:map.end_point[i][1] + 2] = \
        #     np.where(map.mp[0, map.end_point[i][0] - 1:map.end_point[i][0] + 2,map.end_point[i][1] - 1:map.end_point[i][1] + 2] != 15, 1, 15)
        map.ObtainObstacle(a_star1_0.path, 0)
        map.mp[1, map.start_point[i][0], map.start_point[i][1]] = 15   # 将surface的起点标注
    # plt.imshow(map.mp[1])
    # plt.show()
    else:
        map.mp[0, map.end_point[i][0] - 1:map.end_point[i][0] + 2, map.end_point[i][1] - 1:map.end_point[i][1] + 2] = \
            np.where(map.mp[0, map.end_point[i][0] - 1:map.end_point[i][0] + 2,map.end_point[i][1] - 1:map.end_point[i][1] + 2] != 4, 1, 15)




    # plt.imshow(map.mp[1])
    # plt.show()
    # plt.imshow(map.mp[0])
    # plt.show()


plt.imshow(map.mp[1])
plt.show()
plt.imshow(map.mp[0])
plt.show()

end_time = time.time()
print('===== Algorithm finish in', int(end_time-start_time), ' seconds')
#
# a_star2 = a_star.AStar(map.mp[0], 7, 3, 17, 96)
# a_star2.RunAndSaveImage()
# plt.imshow(map.mp[0])
# plt.show()
#
# map.mp[0, 6:9, 3:5] = np.where(map.mp[0, 6:9, 3:5] != 15, 1, map.mp[0, 6:9, 3:5])
# map.ObtainObstacle(a_star2.path)
# plt.imshow(map.mp[0])
# plt.show()

# map.mp[6:9, 3:4] = 6
# map.mp[6:9, 4:5] = 6

# a_star3 = a_star.AStar(map.mp, 11, 7, 21, 27)
# a_star3.RunAndSaveImage()
# plt.imshow(map.mp)
# plt.show()