import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    n,m,k = minput()
    if m<2*k: print('Yuto')
    else:
        if (n*m-2*k*k)&1: print('Yuto')
        else: print('Platina')