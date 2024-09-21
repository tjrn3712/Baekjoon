import sys

a, b = map(int, sys.stdin.readline().rstrip('\n').split())
lines = []
chess1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
chess2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]
for i in range(a):
    lines.append(sys.stdin.readline().rstrip('\n'))

err1 = 2147483647
err2 = 2147483647
temp = []
all = []
for i in range(a - 7):
  for j in range(b - 7):
    ii = 0
    for line_index in range(len(lines)):
      temp.append(lines[line_index + i][j:j + 8])
      ii += 1
      if ii == 8:
        break
    all.append(temp)
    temp = []

# print(all)
for board in all:
    for i in range(len(board)):
        temp1 = 0
        temp2 = 0
        for j in range(8):
            for k in range(8):
                if chess1[j][k] != board[j][k]:
                    temp1 += 1
                else:
                    temp2 += 1
        err1 = min(temp1, err1)
        err2 = min(temp2, err2)


print(min(err1, err2))