import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


while True:
    line = input().strip()
    if line == '#': break

    one = line.count('1')
    if line[-1] == 'o':
        if one&1: print(line[:-1]+'0')
        else: print(line[:-1]+'1')
    else:
        if one&1: print(line[:-1]+'1')
        else: print(line[:-1]+'0')