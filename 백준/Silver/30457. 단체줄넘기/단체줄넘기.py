import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n = int(input())
a = [*minput()]
visited = [0]*1001
ans = len(a)
for i in a:
    if visited[i]: continue
    visited[i] = 1
    ans -= max(0, a.count(i)-2)
print(ans)