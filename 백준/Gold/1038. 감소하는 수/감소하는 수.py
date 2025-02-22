import sys
from itertools import combinations
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
ans = []
for i in range(1,11):
    for j in combinations([*range(10)],i):
        ans.append(int(''.join([*map(str,reversed(j))])))
ans.sort()
try: print(ans[n])
except: print(-1)