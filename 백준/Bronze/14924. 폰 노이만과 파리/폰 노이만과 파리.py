import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


s, t, d = minput()
print(t*(d//(s*2)))