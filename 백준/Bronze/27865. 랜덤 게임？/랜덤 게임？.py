import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
while True:
    print('? 1')
    sys.stdout.flush()
    l = ipt().rstrip('\n')
    if l == 'Y':
        print('! 1')
        sys.exit(0)
