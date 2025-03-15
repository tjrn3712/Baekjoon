import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


for _ in range(int(input())):
    line0 = input().rstrip()
    line = line0.lower()
    g = line.count('g')
    b = line.count('b')

    if g == b:
        print(line0, 'is NEUTRAL')
    elif g > b:
        print(line0, 'is GOOD')
    else:
        print(line0, 'is A BADDY')
