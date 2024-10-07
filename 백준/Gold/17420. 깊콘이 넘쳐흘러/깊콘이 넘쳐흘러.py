import sys
from collections import deque
import math
import heapq
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
a = list(minput())
b = list(minput())
lis = []
for i in range(n):
    lis.append([b[i], a[i]])
cnt = 0
lis.sort()
lis = deque(lis)
while len(lis) != 0:
    if lis[0][1] < lis[0][0]:
        temp = math.ceil((lis[0][0] - lis[0][1])/30)
        cnt += temp
        for j in range(1, len(lis)):
            if lis[j][1] < lis[0][1] + temp * 30:
                temp2 = math.ceil((lis[0][1] + temp * 30 - lis[j][1]) / 30)
                lis[j][1] += 30 * temp2
                cnt += temp2
        
        lis.popleft()
    else:
        for j in range(1, len(lis)):
            if lis[j][1] < lis[0][1]:
                temp2 = math.ceil((lis[0][1] - lis[j][1]) / 30)
                lis[j][1] += 30 * temp2
                cnt += temp2
        
        lis.popleft()
    lis = deque(sorted(list(lis)))
print(cnt)


