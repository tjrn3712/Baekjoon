import sys, math
input = sys.stdin.readline
def minput(): return map(int, input().split())


n, k = minput()
grid = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        grid[i][j] = (i + j) & 1

if k&1:
    grid = [[1]*n for i in range(n)]
else:
    if k == 2:
        for i in range(n):
            for j in range(n):
                grid[i][j] = (i+j)&1
    elif k == 4:
        temp = 0
        for i in range(n):
            temp += 1
            for j in range(n):
                grid[i][j] = 1 if (i+j+temp)&3 else 0
    else:
        temp = 0
        for i in range(n):
            temp += k//2 + 1 if ~(k//2)&1 else k//2
            for j in range(n):
                if (temp+j+1)%k==0:
                    grid[i][j] = 1
for i in grid:
    print(*i)