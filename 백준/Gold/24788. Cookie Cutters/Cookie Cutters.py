import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 998244353
def minput(): return map(int, ipt().split())


def shoelace_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        area += (x_i * y_next) - (x_next * y_i)
    return abs(area) / 2.0


n = int(ipt())
polygon = []
x = mod
y = mod
for i in range(n):
    polygon.append(list(map(float, ipt().split())))
    x = min(polygon[i][0], x)
    y = min(polygon[i][1], y)
area = shoelace_area(polygon)
a = int(ipt())
for i in range(n):
    polygon[i][0] -= x
    polygon[i][1] -= y
    polygon[i][0] *= math.sqrt(a/area)
    polygon[i][1] *= math.sqrt(a/area)
    print(polygon[i][0], polygon[i][1])
