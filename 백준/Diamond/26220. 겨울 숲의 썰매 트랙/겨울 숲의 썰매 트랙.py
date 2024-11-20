import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
p = n // 4
q = n % 4
if n == 3:
    print('4\n1 1\nRDLU')
elif n == 5:
    print('16\n1 2\nRDRDRDLDLULULURU')
elif n == 7:
    print('32\n2 2\nURDRURDRDRDLDRDLDLULDLULULURULUR')
else:
    if q == 1:
        f = ((n-1)//2)**2*4
        print(f)
        print(2,2)
        print('URDR'*(2*p-1)+'DRDL'*(2*p-1)+('DLUL'+'URUL'*(2*p-2)+'ULDL'+'DRDL'*(2*p-2))*(p-1)+'DLUL'+'ULUR'*(2*p-1))
    elif q == 3:
        f = (((n-1)//2)**2-1)*4
        print(f)
        print(2,2)
        print('URDR'*(2*p)+'DRDL'*(2*p)+('DLUL'+'URUL'*(2*p-1)+'ULDL'+'DRDL'*(2*p-1))*(p-1)+'DLUL'+'URULULDLULURURDR'*(p-1)+'URULULDLULUR')
