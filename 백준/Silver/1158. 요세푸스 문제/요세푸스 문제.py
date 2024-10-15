import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k = map(int, sys.stdin.readline().rstrip('\n').split())

people = deque(range(1, n+1))
killed = []

for i in range(n):
    for j in range(k):
        a = people.popleft()
        people.append(a)
        while a == 0:
            a = people.popleft()
            people.append(a)
        if j == k - 1:
            people.pop()
            killed.append(str(a))


print('<', end='')
print(', '.join(killed), end='')
print('>')