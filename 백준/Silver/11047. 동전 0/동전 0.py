import sys
from collections import deque
import math

ipt = sys.stdin.readline

n, k = map(int, ipt().rstrip('\n').split())
coins = []
for i in range(n):
    coins.append(int(ipt()))
coins.reverse()
total = 0
result = 0
for i in range(len(coins)):
    result += (k - total) // coins[i]
    total += ((k - total) // coins[i]) * coins[i]

print(result)