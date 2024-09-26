import sys
from collections import deque
import math
ipt = sys.stdin.readline

s = set()

for i in range(int(ipt())):
    inp = ipt().rstrip('\n').split()
    if 'add' in inp:
        s.add(int(inp[1]))
    elif 'remove' in inp:
        if int(inp[1]) in s:
            s.remove(int(inp[1]))
    elif 'check' in inp:
        if int(inp[1]) in s:
            print(1)
        else:
            print(0)
    elif 'toggle' in inp:
        if int(inp[1]) in s:
            s.remove(int(inp[1]))
        else:
            s.add(int(inp[1]))
    elif 'all' in inp:
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif 'empty' in inp:
        s.clear()
