import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
sys.set_int_max_str_digits(10**9)
def minput(): return map(int, ipt().split())


l = list(ipt().rstrip())
a = l.count('A')
b = l.count('B')
c = l.count('C')
l = ''.join(l)
if a == 0 and b == 0 and c == 0:
    print(l)
elif b == 0 and c == 0:
    print(l)
elif a == 0 and c == 0:
    if b == 1:
        print(l)
    else:
        print(-1)
elif a == 0 and b == 0:
    if c == 1:
        print(l)
    else:
        print(-1)
elif a == 0:
    if (b, c) == (1, 1):
        print(l)
    elif (b, c) == (2, 1):
        print('BCB')
    else:
        print(-1)
elif b == 0:
    if c == 1:
        print(l)
    else:
        if a >= (c-1)*2:
            print('CAA'*(c-1)+'C'+'A'*(a-(c-1)*2))
        else:
            print(-1)
elif c == 0:
    if b == 1:
        print(l)
    else:
        if a >= b-1:
            print('BA'*(b-1)+'B'+'A'*(a-b+1))
        else:
            print(-1)
else:
    if b == 1 and c == 1:
        print(l)
    elif b == 2 and c == 1:
        print('BCB'+'A'*a)
    else:
        temp = min(a, b, c)
        t = 'CBA'*temp
        a -= temp
        b -= temp
        c -= temp
        if (a, b, c) == (0, 0, 0):
            print(t)
        elif (b, c) == (0, 0):
            print(t+'A'*a)
        elif (a, c) == (0, 0):
            if b == 1:
                print('B'+t)
            elif b == 2:
                print('B'+t+'B')
            elif b == temp+1:
                print('B'+'CBAB'*(b-1)+'CBA'*(temp-b))
            elif b < temp+1:
                print('CBAB'*b+'CBA'*(temp-b))
            else:
                print(-1)
        elif (a, b) == (0, 0):
            if c == 1:
                print(t+'C')
            else:
                print(-1)
        elif a == 0:
            if (b, c) == (1, 1):
                print('B'+t+'C')
            elif (b, c) == (2, 1):
                print('B'+t+'CB')
            elif (b, c) == (3, 1):
                print('B'+t+'BCB')
            elif c == 1 and b <= temp+2:
                print('B'+'CBAB'*(b-2)+'CBA'*(temp-b+2)+'CB')
            else:
                print(-1)
        elif b == 0:
            if a >= (c-1)*2:
                print(t+'CAA'*(c-1)+'C'+'A'*(a-(c-1)*2))
            else:
                print(-1)
        elif c == 0:
            if a+temp >= b-1:
                if b > a:
                    print('BA'*a+'B'+'CBAB'*(b-a-1)+'CBA'*(temp+a-b+1))
                else:
                    print('BA'*b+'CBA'*(temp)+'A'*(a-b))
            else:
                print(-1)
