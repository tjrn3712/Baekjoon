import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
w=[*minput()]
w.sort()
wei=0
ans=0
for i in w:
    if i>=wei:
        wei+=i
        ans+=1
print(ans)
