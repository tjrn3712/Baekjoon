import sys
from collections import deque
import math
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, b, c = minput()
a = list(minput())
money = 0
if b <= c:
    money = sum(a) * b
else:
    to_buy = [a[0], min(a[0], a[1]), 0]
    ramen = [[0, min(a[0], a[1]), 0]]
    if ramen[0][1] != a[1]:
        ramen[0][0] = a[1] - ramen[0][1]
        to_buy[0] += a[1] - ramen[0][1]
    ramen = deque(ramen)
    for i in range(2, n):
        ramen.append([0, 0, 0])
        temp = min(ramen[0][0], a[i])
        ramen[1][1] = temp
        to_buy[1] += temp
        if temp == a[i]:
            ramen.popleft()
            continue
        temp2 = min(ramen[0][1], a[i]-temp)
        ramen[1][2] = temp2
        to_buy[2] += temp2
        if temp + temp2 == a[i]:
            ramen.popleft()
            continue
        ramen[1][0] = a[i] - temp - temp2
        ramen.popleft()
        to_buy[0] += a[i] - temp - temp2
    money = to_buy[0] * b + to_buy[1] * c + to_buy[2] * c

print(money)
