import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n = int(input())
ans = [n]
m = -1
for i in range(1, n+1):
    temp = [n, i]
    while temp[-2]-temp[-1]>=0:
        temp.append(temp[-2]-temp[-1])
    if m<len(temp):
        ans = temp
        m = len(temp)
print(m)
print(*ans)