import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


t = int(input())
n = int(input())
f = [*minput()]
if sum(f)>=t: print('Padaeng_i Happy')
else: print('Padaeng_i Cry')