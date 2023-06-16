# a_star.py

import sys
import time

import numpy as np

# from matplotlib.patches import Rectangle

import point
# import pygame
import map
# import random_map

class AStar:
    def __init__(self, map_1, StartPoint_x, StartPoint_y, EndPoint_x, EndPoint_y):
        self.map = map_1
        self.StartPoint_x = StartPoint_x
        self.StartPoint_y = StartPoint_y
        self.EndPoint_x = EndPoint_x
        self.EndPoint_y = EndPoint_y
        self.open_set = []
        self.close_set = []
        self.path = []

    def BaseCost(self, p):
        x_dis = np.abs(p.x - self.StartPoint_x)
        y_dis = np.abs(p.y - self.StartPoint_y)
        # Distance to start point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def HeuristicCost(self, p):
        x_dis = np.abs(self.EndPoint_x - p.x)
        y_dis = np.abs(self.EndPoint_y - p.y)
        # Distance to end point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def TotalCost(self, p):
        return self.BaseCost(p) + self.HeuristicCost(p)

    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= 100 or y >= 100:
            return False
        return not map.IsObstacle(x, y)

    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.x == self.StartPoint_x and p.y == self.StartPoint_y

    def IsEndPoint(self, p):
        return p.x == self.EndPoint_x and p.y == self.EndPoint_y

    def ProcessPoint(self, x, y, parent):
        if not self.IsValidPoint(x, y):
            return # Do nothing for invalid point
        p = point.Point(x, y)
        if self.IsInCloseList(p):
            return # Do nothing for visited point
        print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.IsInOpenList(p):
            p.parent = parent
            p.cost = self.TotalCost(p)
            self.open_set.append(p)

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.TotalCost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p, start_time):
        # path = []
        while True:
            self.path.insert(0, [p.x, p.y]) # Insert first
            if self.IsStartPoint(p):
                break
            else:
                p = p.parent
        for i in range(2, len(self.path) - 2):    #越界
            if i == len(self.path) - 2:
                break
            if self.path[i-1][0] == self.path[i+1][0] and self.path[i][0] == self.path[i-1][0] + 1:
                if not map.IsObstacle(self.path[i][0], self.path[i][1]):
                    self.path[i][0] = self.path[i-1][0]
            if self.path[i-1][0] == self.path[i+1][0] and self.path[i][0] == self.path[i-1][0] - 1:
                if not map.IsObstacle(self.path[i][0], self.path[i][1]):
                    self.path[i][0] = self.path[i-1][0]
        #
        for p in self.path:
            map.mp[0, p[0] : p[0] + 1,p[1]: p[1] + 1] = 15

        # # 获取当前窗口的Surface对象
        # surface = pygame.display.get_surface()
        # # 创建一个新的Surface对象，并将窗口内容复制到其中
        # screenshot = pygame.Surface((300, 300))
        # screenshot.blit(surface, (0, 0))
        # # 将新的Surface对象保存为图像文件
        # pygame.image.save(screenshot, "routed.png")
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time-start_time), ' seconds')

    def RunAndSaveImage(self):
        start_time = time.time()

        start_point = point.Point(self.StartPoint_x, self.StartPoint_y)
        start_point.cost = 0
        self.open_set.append(start_point)

        while True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            p = self.open_set[index]
            # rec = Rectangle((p.x, p.y), 1, 1, color='c')
            # ax.add_patch(rec)
            # self.SaveImage(plt)

            # 画openlist
            # pygame.draw.circle(map.screen, map.GREY, (p.x, p.y), 1)

            if self.IsEndPoint(p):
                return self.BuildPath(p, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            # Process all neighbors
            x = p.x
            y = p.y
            self.ProcessPoint(x-1, y+1, p)
            self.ProcessPoint(x-1, y, p)
            self.ProcessPoint(x-1, y-1, p)
            self.ProcessPoint(x, y-1, p)
            self.ProcessPoint(x+1, y-1, p)
            self.ProcessPoint(x+1, y, p)
            self.ProcessPoint(x+1, y+1, p)
            self.ProcessPoint(x, y+1, p)

