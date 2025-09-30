import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


q = int(input())
for _ in range(q):
    n, x, y = minput()
    t = (n*y)%(x+y)
    if t: print(2, (n*y-t)//(x+y), x+y-t, (n*y-t)//(x+y)+1, t)
    else: print(1, (n*y-t)//(x+y), x+y)