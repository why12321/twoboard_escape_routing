# 1障碍 6虚拟节点 9pin
import numpy as np
import matplotlib.pyplot as plt
import os

mp = np.zeros((30,30))

n = [3, 7, 11, 15,19,23,27,30]
for j in n:
    for i in n:
        mp[j:j+1,i:i+1]=9

m = [5,9,13,17,21,25]

for x in m:
    for y in n:
        mp[x:x + 1, y:y+1] = 6
for x in n:
    for y in m:
        mp[x:x + 1, y:y+1] = 6
for a in m:
    for b in m:
        mp[a:a + 1, b:b + 1] = 6
for x in m:
    mp[x:x + 1,3:27] = 6
    mp[ 3:27,x:x + 1] = 6
mp[14:15, 10:13] = 6
# mp[10:13,14:15] = 6
mp[16:17,10:13] = 6
# mp[10:13,16:17] = 6
mp[15:16,10:11] = 6
mp[15:16,12:13] = 6
mp[15:16,11:12]= 4



mp[0,:]=1
mp[-1,:]=1
mp[:,0]=1
mp[:,-1]=1





# plt.imshow(mp)
# plt.show()

if not os.path.exists('./data'):
    os.makedirs('./data')
np.save('./data/mp.npy',mp)


def IsObstacle(i, j):
    if mp[i, j] == 1 or mp[i, j] == 9 or mp[i, j] == 0:
        return True
    return False