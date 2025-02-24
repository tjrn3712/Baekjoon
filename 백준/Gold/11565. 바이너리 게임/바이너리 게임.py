import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


a = input().rstrip()
b = input().rstrip()

ac = a.count('1')
bc = b.count('1')
if (ac>=bc) or (ac&1 and bc-ac==1): print('VICTORY')
else: print('DEFEAT')