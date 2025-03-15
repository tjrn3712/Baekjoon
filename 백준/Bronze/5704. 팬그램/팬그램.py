import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


while True:
    line = input().strip()
    if line == '*' : break
    a = [False]*26

    for n in line:
        for c in 'qwertyuiopasdfghjklzxcvbnm':
            i = ord(c)-97
            if n == c: a[i] = True

    ans = True
    for i in range(26):
        ans &= a[i]

    if ans: print('Y')
    else: print('N')