import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
if (n-6)%5==0:
    print("Yes")
    ans=[0,1,2,0,1,2]
    while 1:
        if len(ans)==n:
            exit(print(*ans))
        if ans[-1]==2:
            ans.extend([1,0,2,1,0])
        elif ans[-1]==0:
            ans.extend([1,2,0,1,2])
else: print("No")
