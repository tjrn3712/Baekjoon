import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


for i in range(int(ipt())):
    person = [[]]
    num = int(ipt())
    for j in range(num):
        person.append(int(ipt()))
    nex = 1
    count = 0
    while True:
        count += 1
        nex = person[nex]
        if nex == num:
            print(count)
            break
        if nex == 1:
            print(0)
            break
        if count > nex+1:
            print(0)
            break
