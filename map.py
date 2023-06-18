# 1障碍 6虚拟节点 9pin
import numpy as np
import matplotlib.pyplot as plt
import os

mp = np.zeros((2, 100, 100))

# map[0] --- base层
n=[]
for i in range(25):
    n.append(4 * i - 1)
for j in n:
    for i in n:
        mp[0, j:j+1,i:i+1]=9

m=[]
for i in range(24):
    m.append(4 * i + 1)

for x in m:
    for y in n:
        mp[0, x:x + 1, y:y+1] = 6
for x in n:
    for y in m:
        mp[0, x:x + 1, y:y+1] = 6
for a in m:
    for b in m:
        mp[0, a:a + 1, b:b + 1] = 6
for x in m:
    mp[0, x:x + 1,3:97] = 6
    mp[0, 3:97, x:x + 1] = 6
# mp[0, 14:15, 10:13] = 6
# mp[10:13,14:15] = 6
# mp[0, 16:17, 10:13] = 6
# mp[10:13,16:17] = 6
# mp[0, 15:16, 10:11] = 6
# mp[0, 15:16, 12:13] = 6
# mp[0, 6:9, 3:4] = 6
# mp[0, 6:9, 4:5] = 6

# mp[0, 15:16,11:12]= 4
# mp[0, 7:8,3:4] = 4



mp[0, 0,:]=1
mp[0, -1,:]=1
mp[0, :,0]=1
mp[0, :,-1]=1


k = [36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62]
l = [37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61]

for j in k:
    mp[1, 38:39,j:j+1] = 9
for i in l:
    mp[1, 42:43,i:i+1] = 9


a=[48,50]
for i in a:
    mp[1, 45:46, i:i + 1] = 9
    mp[1, 48:49, i:i + 1] = 9
    mp[1, 51:52, i:i + 1] = 9
    mp[1, 54:55, i:i + 1] = 9


for j in l:
    mp[1, 61:62,j:j+1] = 9
    mp[1, 59:60, j:j + 1] = 9
for i in k:
    mp[1, 57:58, i:i + 1] = 9


# mp[36:37,0:30] = 6
mp[1, 40:41,0:100] = 6
mp[1, 44:45,35:47] = 6
mp[1, 45:56,35:47] = 6
mp[1, 44:56,52:65] = 6
# mp[24:25,0:30] = 6
# mp[28:29,0:30] = 6
mp[1, :,0:35] = 6
mp[1, :,65:100] = 6
mp[1, 0:37,:] = 6
mp[1, 63:100,:] = 6

mp[1, 0,:]=1
mp[1, -1,:]=1
mp[1, :,0]=1
mp[1, :,-1]=1


# plt.imshow(mp[0])
# plt.show()
# plt.imshow(mp[1])
# plt.show()

start_point = [[38, 40], [59, 41], [42, 51], [54, 48], [61, 37], [59, 49], [57, 40], [38, 45]]
end_point = [[39, 19], [79, 83], [79, 79], [95, 83], [11, 11], [63, 95], [19, 19], [79, 23]]

if not os.path.exists('./data'):
    os.makedirs('./data')
np.save('./data/mp[0].npy',mp[0])
if not os.path.exists('./data'):
    os.makedirs('./data')
np.save('./data/mp[1].npy',mp[1])


def IsObstacle(i, j, k):
    if mp[i, j, k] == 1 or mp[i, j, k] == 9 or mp[i, j, k] == 0 or mp[i, j, k] == 15:
        return True
    return False

def ObtainObstacle(path,j):
    for i in range(0, len(path)):
        if mp[j, path[i][0] - 1, path[i][1] + 1] != 15:
            mp[j, path[i][0] - 1, path[i][1] + 1] = 1
        if mp[j, path[i][0] - 1, path[i][1]] != 15:
            mp[j, path[i][0] - 1, path[i][1]] = 1
        if mp[j, path[i][0] - 1, path[i][1] - 1] != 15:
            mp[j, path[i][0] - 1, path[i][1] - 1] = 1
        if mp[j, path[i][0], path[i][1] - 1] != 15:
            mp[j, path[i][0], path[i][1] - 1] = 1
        if mp[j, path[i][0] + 1, path[i][1] - 1] != 15:
            mp[j, path[i][0] + 1, path[i][1] - 1] = 1
        if mp[j, path[i][0] + 1, path[i][1]] != 15:
            mp[j, path[i][0] + 1, path[i][1]] = 1
        if mp[j, path[i][0] + 1, path[i][1] + 1] != 15:
            mp[j, path[i][0] + 1, path[i][1] + 1] = 1
        if mp[j, path[i][0], path[i][1] + 1] != 15:
            mp[j, path[i][0], path[i][1] + 1] = 1



def point_is_available(i, point_x, point_y):
    if mp[i, point_x - 1, point_y + 1] == 9 or mp[i, point_x - 1, point_y] == 9 \
       or mp[i, point_x - 1, point_y - 1] == 9 or mp[i, point_x, point_y - 1] == 9 \
       or mp[i, point_x + 1, point_y - 1] == 9 or mp[i, point_x + 1, point_y] == 9 \
       or mp[i, point_x + 1, point_y + 1] == 9 or mp[i, point_x, point_y + 1] == 9:
        return False
    return True



def set_start_end_point_routable(i, start_end_point_x, start_end_point_y):
    if point_is_available(i, start_end_point_x - 1, start_end_point_y + 1):
        mp[i, start_end_point_x - 1, start_end_point_y + 1] = 6
    if point_is_available(i, start_end_point_x - 1, start_end_point_y):
        mp[i, start_end_point_x - 1, start_end_point_y] = 6
    if point_is_available(i, start_end_point_x - 1, start_end_point_y - 1):
        mp[i, start_end_point_x - 1, start_end_point_y - 1] = 6
    if point_is_available(i, start_end_point_x, start_end_point_y - 1):
        mp[i, start_end_point_x, start_end_point_y - 1] = 6
    if point_is_available(i, start_end_point_x + 1, start_end_point_y - 1):
        mp[i, start_end_point_x + 1, start_end_point_y - 1] = 6
    if point_is_available(i, start_end_point_x + 1, start_end_point_y):
        mp[i, start_end_point_x + 1, start_end_point_y] = 6
    if point_is_available(i, start_end_point_x + 1, start_end_point_y + 1):
        mp[i, start_end_point_x + 1, start_end_point_y + 1] = 6
    if point_is_available(i, start_end_point_x, start_end_point_y + 1):
        mp[i, start_end_point_x, start_end_point_y + 1] = 6