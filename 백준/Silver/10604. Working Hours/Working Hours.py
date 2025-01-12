import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


now=0
while True:
    s = input().rstrip('\n')
    temp = 0
    if s == '###':
        if now%60 >= 10:
            print(now//60, ':', now%60, sep='')
        else:
            print(now//60, ':0', now%60, sep='')
        break
    if s == '$$$':
        if now%60 >= 10:
            print(now//60, ':', now%60, sep='')
        else:
            print(now//60, ':0', now%60, sep='')
        now=0
        continue
    if ':' in s:
        a = s[1:].split(':')
    else:
        a = s[1:].split('.')
    if len(a[0]):
        temp += int(a[0])*60
    if len(a[1]):
        temp += int(a[1])
    if s[0] == '+':
        now += temp
    else:
        now -= temp