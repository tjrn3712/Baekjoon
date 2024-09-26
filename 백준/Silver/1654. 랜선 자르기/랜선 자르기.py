import sys
from collections import deque
import math

k, m = map(int, sys.stdin.readline().rstrip('\n').split())

lines = []
for i in range(k):
    lines.append(int(sys.stdin.readline()))

right = sum(lines) // m
left = 1

while True:
    temp = sum([i // ((right + left) // 2) for i in lines])
    if temp >= m:
        left = (right + left) // 2
    else:
        right = (right + left) // 2

    if right - left == 1 or right == left:
        break


if sum([i // right for i in lines]) < m:
    result = left
else:
    result = right

print(result)
