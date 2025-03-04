import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
now = set()
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'enter':
        now.add(a)
    else:
        if a in now:
            now.remove(a)
now = [*now]
now.sort(reverse=True)
print(*now, sep='\n')