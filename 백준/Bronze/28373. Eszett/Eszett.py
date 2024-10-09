import sys
from collections import deque
import math
ipt = sys.stdin.readline
sys.setrecursionlimit(10**9)
def minput(): return map(int, ipt().split())


s = ipt().rstrip('\n')
s = s.lower()
print(s)
if 'sss' in s:
    print(s.replace('sss', 'Bs'))
    print(s.replace('sss', 'sB'))
elif 'ss' in s:
    print(s.replace('ss', 'B'))
