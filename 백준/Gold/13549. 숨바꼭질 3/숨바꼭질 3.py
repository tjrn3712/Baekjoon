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
        for _ in range(len(q)):
            i = q.popleft()
            if i<=50000 and not visited[2*i]:
                if grid[2*i] == 998244353:
                    return grid[i]
                q.append(2*i)
                grid[2*i]=grid[i]
                visited[2*i] = True
            if i>0 and not visited[i-1]:
                if grid[i-1] == 998244353:
                    return grid[i]+1
                q.append(i-1)
                grid[i-1]=grid[i]+1
                visited[i-1] = True
            if i<100000 and not visited[i+1]:
                if grid[i+1] == 998244353:
                    return grid[i]+1
                q.append(i+1)
                grid[i+1]=grid[i]+1
                visited[i+1] = True
 

 
n, k = minput()
if n == k:
    print(0)
    sys.exit()
grid = [0]*100001
grid[n], grid[k] = 0, 998244353
visited = [False]*100001
visited[n] = True
q = deque([n])
print(bfs(grid, visited))
