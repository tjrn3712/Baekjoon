import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())

t=int(input())
for _ in range(t):
    p=input().strip()
    n=int(input())
    a=[*input().strip()[1:-1].split(',')]
    if not n: a=[]
    dq=deque(a)
    rev=0
    err=0
    for i in p:
        if i=='R': rev^=1
        else:
            if dq:
                if rev: dq.pop()
                else: dq.popleft()
            else: err=1;break
    if err:print('error')
    else:
        if rev: dq.reverse()
        print('[',end='')
        print(*dq,sep=',',end='')
        print(']')