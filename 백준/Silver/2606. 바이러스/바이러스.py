import sys
from collections import deque
import math
ipt = sys.stdin.readline

coms = set()
coms.add(1)
o = []

ipt()
for i in range(int(ipt())):
    a, b = map(int, ipt().rstrip('\n').split())
    o.append((a, b))

while True:
    p = False
    for i in range(len(o)):
        if o[i][0] in coms or o[i][1] in coms:
            coms.add(o[i][0])
            coms.add(o[i][1])
            p = True
            del o[i]
            break
    if not p:
        break

print(len(coms) - 1)