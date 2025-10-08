import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m,k = minput()
print(min(n.bit_length()-1,m+k.bit_length()-1))