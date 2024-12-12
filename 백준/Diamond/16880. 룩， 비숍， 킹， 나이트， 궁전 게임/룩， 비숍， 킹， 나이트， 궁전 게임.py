import sys, time, math, heapq, random, itertools
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.set_int_max_str_digits(10**9)
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
grundies = []
for _ in range(n):
    x, y, o = input().split()
    x, y = int(x), int(y)
    if o == 'P':
        grundies.append(((x//3)^(y//3))*3+(x+y)%3)
    elif o == 'B':
        grundies.append(min(x, y))
    elif o == 'R':
        grundies.append(x^y)
    elif o == 'K':
        grundies.append((min(x, y)%2)*2+abs(x-y)%2)
    elif o == 'N':
        if min(x, y)%3 == 0:
            gr = 0
        elif min(x, y)%3 == 1:
            gr = 0 if x == y else 1
        else:
            gr = 1 if abs(x-y) < 2 else 2
        grundies.append(gr)

tmp = 0
for i in range(n):
    tmp ^= grundies[i]
if tmp:
    print('koosaga')
else:
    print('cubelover')