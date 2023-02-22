import math
import random
from functools import cmp_to_key
from math import atan2
from time import time
import matplotlib.pyplot as plt
import numpy


def PairsConvexHull(points):
    hull = []
    for p in points:
        for q in points:
            if p != q:
                W = q[0] - p[0]
                H = q[1] - p[1]
                isLeft = True
                for k in points:
                    if W * (k[1] - p[1]) - H * (k[0] - p[0]) < 0:   # implicit line equation
                        isLeft = False
                        break
                if isLeft:
                    hull.append(p)
                    hull.append(q)
    res = []
    [res.append(x) for x in hull if x not in res]  # remove duplicates
    return res

refvec = [1, 0]

def angularCompare(p, q):
    return q[1] - p[1]

def GrahamScan(points):
    res = []
    [res.append(x) for x in points if x not in res]
    p0 = points[0]
    for p in points:
        if p[1] < p0[1] or (p[1] == p0[1] and p[0] > p0[0]):
            p0 = p
    index = points.index(p0)
    temp = points[0]
    points[0] = p0
    points[index] = temp
    pointsAngles = []
    for i in range(1, len(points)):
        # theta = acos((u dot v)/(||u|| ||v||))
        angle = math.acos(numpy.dot([1, 0], [points[i][0]-p0[0], points[i][1]-p0[1]])/math.sqrt(math.pow(points[i][0]-p0[0], 2)+math.pow(points[i][1]-p0[1], 2)))
        pointsAngles.append([points[i], angle])
    pointsAngles.insert(0, [p0, 0])
    pointsAngles = sorted(pointsAngles, key=cmp_to_key(angularCompare), reverse=True)
    d2 = math.sqrt(math.pow(points[i][0], 2) + math.pow(points[i][1], 2))
    length = len(pointsAngles) - 1
    j = 0
    while j < length:
        if pointsAngles[j][1] == pointsAngles[j+1][1]:
            d1 = math.sqrt(math.pow(pointsAngles[j][0][0], 2) + math.pow(pointsAngles[j][1], 2))
            d2 = math.sqrt(math.pow(pointsAngles[j + 1][0][0], 2) + math.pow(pointsAngles[j + 1][1], 2))
            if d1 < d2:
                pointsAngles.remove(pointsAngles[j])
                j -= 1
            else:
                pointsAngles.remove(pointsAngles[j+1])
                j -= 1
            length -= 1
        j += 1
    stack = []
    stack.append(pointsAngles[0][0]), stack.append(pointsAngles[1][0])
    for i in range(2, len(pointsAngles)):
        p = stack[len(stack) - 1]
        q = stack[len(stack) - 2]
        while ((pointsAngles[i][0][0] - q[0]) * (p[1] - q[1]) - (pointsAngles[i][0][1] - q[1]) *
                (p[0] - q[0]) >= 0) and (len(stack) > 2):
            stack.pop()
            p = q
            q = stack[len(stack) - 2]
        stack.append(pointsAngles[i][0])
    stack.append(p0)
    return stack

if __name__ == '__main__':
    random.seed()
    points = []
    for i in range(1000):
        points.append([random.randrange(-10000, 10000), random.randrange(-10000, 10000)])
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, 'bo')
    plt.show()
    start = time()
    stack = GrahamScan(points)
    end = time()
    print(end - start, "\n")
    x = []
    y = []
    for p in stack:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, '--r')
    plt.show()
    points = []
    for i in range(10000):
        points.append([random.randrange(-10000, 10000), random.randrange(-10000, 10000)])
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, 'bo')
    plt.show()
    start = time()
    stack = GrahamScan(points)
    end = time()
    print(end - start, "\n")
    x = []
    y = []
    for p in stack:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, '--r')
    plt.show()
    points = []
    for i in range(100000):
        points.append([random.randrange(-100000, 100000), random.randrange(-100000, 100000)])
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, 'bo')
    plt.show()
    start = time()
    stack = GrahamScan(points)
    end = time()
    print(end - start, "\n")
    x = []
    y = []
    for p in stack:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, '--r')
    plt.show()
    points = []
    for i in range(1000000):
        points.append([random.randrange(-1000000, 1000000), random.randrange(-1000000, 1000000)])
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, 'bo')
    plt.show()
    start = time()
    stack = GrahamScan(points)
    end = time()
    print(end - start, "\n")
    x = []
    y = []
    for p in stack:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, '--r')
    plt.show()