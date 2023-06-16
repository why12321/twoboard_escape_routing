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
mp[0, 14:15, 10:13] = 6
# mp[10:13,14:15] = 6
mp[0, 16:17, 10:13] = 6
# mp[10:13,16:17] = 6
mp[0, 15:16, 10:11] = 6
mp[0, 15:16, 12:13] = 6
mp[0, 6:9, 3:4] = 6
mp[0, 6:9, 4:5] = 6

mp[0, 15:16,11:12]= 4
mp[0, 7:8,3:4] = 4



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


plt.imshow(mp[0])
plt.show()
plt.imshow(mp[1])
plt.show()

if not os.path.exists('./data'):
    os.makedirs('./data')
np.save('./data/mp[0].npy',mp[0])
if not os.path.exists('./data'):
    os.makedirs('./data')
np.save('./data/mp[1].npy',mp[1])


def IsObstacle(i, j):
    if mp[0, i, j] == 1 or mp[0, i, j] == 9 or mp[0, i, j] == 0 or mp[0, i, j] == 15:
        return True
    return False

def ObtainObstacle(path):
    for i in range(0, len(path) - 2):
        if path[i][0] + 1 == path[i+1][0] and path[i][1] - 1 == path[i+1][1]:
            mp[0, path[i][0], path[i][1] - 1] = 1
            mp[0, path[i][0] + 1, path[i][1]] = 1
        if path[i][0] - 1 == path[i+1][0] and path[i][1] - 1 == path[i+1][1]:
            mp[0, path[i][0], path[i][1] - 1] = 1
            mp[0, path[i][0] - 1, path[i][1]] = 1
        if path[i][0] - 1 == path[i+1][0] and path[i][1] + 1 == path[i+1][1]:
            mp[0, path[i][0], path[i][1] + 1] = 1
            mp[0, path[i][0] - 1, path[i][1]] = 1
        if path[i][0] + 1 == path[i+1][0] and path[i][1] + 1 == path[i+1][1]:
            mp[0, path[i][0], path[i][1] + 1] = 1
            mp[0, path[i][0] + 1, path[i][1]] = 1
