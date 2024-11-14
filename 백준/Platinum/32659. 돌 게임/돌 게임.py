import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())



l = ipt().rstrip('\n')
f = False
ll = False
if l[0] == '.':
    f = True
if l[-1] == '.':
    ll = True
l = l.replace('B', 'W').split('W')
if f:
    l[0] = ''
if ll:
    l[-1] = ''
temp = []
for i in range(1, len(l), 2):
    temp.append(len(l[i]))
tmp = 0
for i in temp:
    tmp ^= i
if tmp:
    print('Win')
else:
    print('Lose')