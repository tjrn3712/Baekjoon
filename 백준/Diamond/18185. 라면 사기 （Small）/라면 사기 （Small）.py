import sys
from collections import deque
import math
ipt = sys.stdin.readline
sys.setrecursionlimit(10**9)
def minput(): return map(int, ipt().split())



n = int(ipt())
a = list(minput())
ramen = []
for i in range(n):
    ramen.append([0, 0, 0])
money = 0
ramen[0] = [a[0], 0, 0]
ramen[1] = [0, min(a[0], a[1]), 0]
if ramen[1][1] != a[1]:
    ramen[1][0] = a[1] - ramen[1][1]
for i in range(2, n):
    temp = min(ramen[i-1][0], a[i])
    ramen[i][1] = temp
    if temp == a[i]:
        continue
    temp2 = min(ramen[i-1][1], a[i]-temp)
    ramen[i][2] = temp2
    if temp + temp2 == a[i]:
        continue
    ramen[i][0] = a[i] - temp - temp2

for i in ramen:
    money += i[0] * 3 + i[1] * 2 + i[2] * 2
print(money)