import sys
from math import factorial as f
input = sys.stdin.readline
sys.set_int_max_str_digits(2000000)
def minput(): return map(int, input().split())


n = int(input())
l = 0
r = 210000
while l<=r:
    mid = (l+r)//2
    fact = f(mid)
    if fact==n: break
    if fact>n: r = mid+1
    else: l = mid-1


print(mid)