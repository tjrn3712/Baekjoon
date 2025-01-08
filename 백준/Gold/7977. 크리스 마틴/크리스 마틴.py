import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
dna = list(input().rstrip('\n'))
ans = [dna.count('A'), dna.count('G'), dna.count('C'), dna.count('T')]
print(min(ans))
print(('AGCT'[ans.index(min(ans))])*n)