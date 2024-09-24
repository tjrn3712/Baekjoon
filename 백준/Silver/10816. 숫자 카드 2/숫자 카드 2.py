import sys

sys.stdin.readline()
a = list(map(int, sys.stdin.readline().rstrip('\n').split()))

sys.stdin.readline()
temp = list(map(int, sys.stdin.readline().rstrip('\n').split()))
dic = dict()
for i in a:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

result = []
for i in temp:
    if i in dic.keys():
        result.append(str(dic[i]))
    else:
        result.append('0')

print(' '.join(result))
