import sys
from collections import deque
import math

grid = [[0] * 100 for i in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip('\n').split())

    for j in range(y1, y2):
        for k in range(x1, x2):
            grid[j][k] = 1

area = 0
for i in grid:
    area += i.count(1)

print(area)
