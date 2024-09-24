import sys
from collections import deque
import math

all = []
alld = dict()
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    all.append(a)
    if a in alld:
        alld[a] += 1
    else:
        alld[a] = 1

all.sort()
for i in all:
    if i in alld:
        alld[i] += 1
    else:
        alld[i] = 1
print(math.floor(sum(all) / len(all) + 0.5))
print(all[len(all) // 2])
a = 0
temp = 0
b = 0
for i in alld.keys():
    a = max(a, alld[i])

s = []
for i in alld.keys():
    if alld[i] == a:
        s.append(i)

s.sort()
if len(s) == 1:
    print(s[0])
else:
    print(s[1])

print(all[-1] - all[0])
