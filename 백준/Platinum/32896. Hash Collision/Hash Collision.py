import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
x = 1
print('?', n, x)
sys.stdout.flush()
c = int(input())
if c==n:
    print('!', c, x)
    sys.stdout.flush()
    sys.exit()
print('?', n-c, x)
sys.stdout.flush()
r = int(input())
print('!', c, r)
sys.stdout.flush()