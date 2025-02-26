import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


while True:
    grid = []
    FEN = input()
    if FEN == '': break
    FEN = FEN.rstrip()
    rows = FEN.split('/')
    for r in rows:
        temp = []
        for i in r:
            if i.isdigit():
                for _ in range(int(i)): temp.append('.')
            else: temp.append(i)
        grid.append(temp[:])

    ans = [[1]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if grid[i][j] != '.': ans[i][j]=0
            if grid[i][j] in 'kK':
                for di in range(-1,2):
                    for dj in range(-1,2):
                        ni=i+di;nj=j+dj
                        if -1<ni<8 and -1<nj<8: ans[ni][nj]=0
            elif grid[i][j] in 'rR':
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni,nj=i,j
                    while True:
                        ni+=di;nj+=dj
                        if not (-1<ni<8 and -1<nj<8):break
                        ans[ni][nj]=0
                        if grid[ni][nj]!='.':break
            elif grid[i][j] in 'Nn':
                for di,dj in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
                    ni=i+di;nj=j+dj
                    if -1<ni<8 and -1<nj<8:ans[ni][nj]=0
            elif grid[i][j] in 'bB':
                for di,dj in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                    ni,nj=i,j
                    while 1:
                        ni+=di;nj+=dj
                        if not (-1<ni<8 and -1<nj<8):break
                        ans[ni][nj]=0
                        if grid[ni][nj]!='.':break
            elif grid[i][j] == 'P':
                for di,dj in [(-1,-1),(-1,1)]:
                    ni=i+di;nj=j+dj
                    if -1<ni<8 and -1<nj<8: ans[ni][nj]=0
            elif grid[i][j] == 'p':
                for di,dj in [(1,-1),(1,1)]:
                    ni=i+di;nj=j+dj
                    if -1<ni<8 and -1<nj<8: ans[ni][nj]=0
            elif grid[i][j] in 'qQ':
                for di,dj in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                    ni,nj=i,j
                    while 1:
                        ni+=di;nj+=dj
                        if not (-1<ni<8 and -1<nj<8):break
                        ans[ni][nj]=0
                        if grid[ni][nj]!='.':break
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni,nj=i,j
                    while True:
                        ni+=di;nj+=dj
                        if not (-1<ni<8 and -1<nj<8):break
                        ans[ni][nj]=0
                        if grid[ni][nj]!='.':break

    cnt = 0
    for i in range(8):
        cnt += sum(ans[i])
    print(cnt)