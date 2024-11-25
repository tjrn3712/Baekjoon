import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


def line_segment_intersection(p):
    v = [0, 0, 0, 0]
    cross_lst = [[0, 2], [0, 3], [1, 2], [1, 3], [2, 0], [2, 1], [3, 0], [3, 1]]
    for i in range(4):
        p1 = [p[cross_lst[2*i][0]][j] - p[cross_lst[2*i][1]][j] for j in [0, 1]]
        p2 = [p[cross_lst[2*i+1][0]][j] - p[cross_lst[2*i+1][1]][j] for j in [0, 1]]
        v[i] = p1[0] * p2[1] - p2[0] * p1[1]
    if sum(vv ** 2 for vv in v) == 0:
        for i in range(2):
            if min(p[2][i], p[3][i]) <= max(p[0][i], p[1][i]) and min(p[0][i], p[1][i]) <= max(p[2][i], p[3][i]) and len(set(p[j][i] for j in range(4))) > 1:
                return True
        else:
            return False
    else:
        return v[0] * v[1] <= 0 and v[2] * v[3] <= 0

n = int(input())
lines = []
for _ in range(n):
    theta1, theta2 = minput()
    r = 1000
    lines.append([[r*math.cos(theta1*2*math.pi/3600), r*math.sin(theta1*2*math.pi/3600)], [r*math.cos(theta2*2*math.pi/3600), r*math.sin(theta2*2*math.pi/3600)]])
theta, r = minput()
p1 = [r*math.cos(theta*2*math.pi/3600), r*math.sin(theta*2*math.pi/3600)]
theta, r = minput()
p2 = [r*math.cos(theta*2*math.pi/3600), r*math.sin(theta*2*math.pi/3600)]
cnt = 0
for i in range(n):
    if line_segment_intersection([p1, p2, lines[i][0], lines[i][1]]):
        cnt += 1
if cnt&1:
    print('NO')
else:
    print('YES')