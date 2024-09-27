import sys
from collections import deque
import math
ipt = sys.stdin.readline

n = int(ipt())
people = list(map(int, ipt().split()))
total = 0
people.sort()
j = 0
for i in range(n, 0, -1):
    total += people[j]*i
    j += 1

print(total)