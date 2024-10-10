import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
bulsang = list(minput())
ggaedareum_offsetedright = []
c = 0
for dol in bulsang:
    if dol == 1:
        ggaedareum_offsetedright.append(c - 1)
        c-=1
    else:
        ggaedareum_offsetedright.append(c + 1)
        c+=1
haetaleui_gyeongji = 1
ggaedareum_offseted_rightmax = 0
ggaedareum_offseted_leftmax = 0
for status in ggaedareum_offsetedright:
    haetaleui_gyeongji = max(haetaleui_gyeongji, abs(status - ggaedareum_offseted_rightmax), abs(status - ggaedareum_offseted_leftmax))
    ggaedareum_offseted_rightmax = max(ggaedareum_offseted_rightmax, status)
    ggaedareum_offseted_leftmax = min(ggaedareum_offseted_leftmax, status)
print(haetaleui_gyeongji)

