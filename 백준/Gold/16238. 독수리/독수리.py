n=int(input());a=[*map(int,input().split())];ans=0
a.sort()
for _ in range(n):ans+=max(a[-_-1]-_,0)
print(ans)