import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(grid, visited):
    temp = 0
    while q:
        temp += 1
        for _ in range(len(q)):
            i = q.popleft()
            if i>0 and not visited[i-1]:
                if grid[i-1] == 2:
                    return temp
                q.append(i-1)
                visited[i-1] = True
            if i<100000 and not visited[i+1]:
                if grid[i+1] == 2:
                    return temp
                q.append(i+1)
                visited[i+1] = True
            if i<=50000 and not visited[2*i]:
                if grid[2*i] == 2:
                    return temp
                q.append(2*i)
                visited[2*i] = True


n, k = minput()
if n == k:
    print(0)
    sys.exit()
grid = [0]*100001
grid[n], grid[k] = 1, 2
visited = [False]*100001
visited[n] = True
q = deque([n])
print(bfs(grid, visited))
