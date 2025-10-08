import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


while 1:
    n = int(input())
    if not n: break

    a = [0]*(n+1)
    s = input().split(',')
    for i in range(len(s)):
        s[i] = [*map(int, s[i].split('-'))]

    for i in range(len(s)):
        if len(s[i])==1:
            if s[i][0]>n:continue
            a[s[i][0]]+=1
            continue
        l,r = s[i]
        for j in range(l,r+1):
            if j>n: break
            a[j]+=1

    ans = 0
    for i in a:
        if i: ans+=1
    print(ans)
