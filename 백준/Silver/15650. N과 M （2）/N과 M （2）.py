import sys, time, math, heapq, random, itertools
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


def dfs(k):
    global temp
    if len(temp) == m:
        ans.append(sorted([*temp]))
        return
    for i in range(k, n+1):
        if i not in temp:
            temp.append(i)
            dfs(i+1)
            temp.pop()


n, m = minput()
temp = []
ans = []
dfs(1)
ans.sort()
for i in range(len(ans)):
    print(*ans[i])