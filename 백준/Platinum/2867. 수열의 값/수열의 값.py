import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

lmax = [-1] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()
    lmax[i] = stack[-1] if stack else -1
    stack.append(i)

rmax = [n] * n
stack = []
for i in range(n-1, -1, -1):
    while stack and a[stack[-1]] <= a[i]:
        stack.pop()
    rmax[i] = stack[-1] if stack else n
    stack.append(i)

ans = 0
for i in range(n):
    left_count = i - lmax[i]
    right_count = rmax[i] - i
    ans += a[i] * left_count * right_count

lmin = [-1] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] > a[i]:
        stack.pop()
    lmin[i] = stack[-1] if stack else -1
    stack.append(i)

rmin = [n] * n
stack = []
for i in range(n-1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    rmin[i] = stack[-1] if stack else n
    stack.append(i)

for i in range(n):
    left_count = i - lmin[i]
    right_count = rmin[i] - i
    ans -= a[i] * left_count * right_count


print(ans)