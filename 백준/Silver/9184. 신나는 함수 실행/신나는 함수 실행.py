import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


func = dict()
func[(-1,-1,-1)], func[(0,-1,-1)], func[(-1,0,-1)], func[(-1,-1,0)], func[(0,0,-1)], func[(0,-1,0)], func[(-1,0,0)], func[(0,0,0)] = 1,1,1,1,1,1,1,1
for i in range(-1, 1):
    for _ in range(21):
        for __ in range(21):
            func[(__,_,i)] = 1
            func[(__,i,_)] = 1
            func[(i,_,__)] = 1
            func[(_,i,__)] = 1
            func[(_,__,i)] = 1
            func[(i,__,_)] = 1
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i*j*k == 0:
                pass
            elif i<j and j<k:
                func[(i,j,k)] = func[(i,j,k-1)] + func[(i,j-1,k-1)] - func[(i,j-1,k)]
            else:
                func[(i,j,k)] = func[(i-1,j,k)] + func[(i-1,j,k-1)] + func[(i-1,j-1,k)] - func[(i-1,j-1,k-1)]

while True:
    a, b, c = minput()
    if a==-1 and b==-1 and c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        res = 1
    elif a>20 or b>20 or c>20:
        res = func[(20,20,20)]
    else:
        res = func[(a,b,c)]
    print('w', (a, b, c), ' = ', res, sep='')

