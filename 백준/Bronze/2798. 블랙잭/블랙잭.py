import sys

N, M = map(int, sys.stdin.readline().strip('\n').split())
cardlist = list(map(int, sys.stdin.readline().strip('\n').split()))
cardlist.sort()

cardlist2 = []

for i in cardlist:
    for j in cardlist:
        for k in cardlist:
            if i != j and j != k and k != i:
                cardlist2.append(i+j+k)
result = 0
cardlist2.sort()
for ii in cardlist2:
    if ii > M:
        break
    result = ii

print(result)