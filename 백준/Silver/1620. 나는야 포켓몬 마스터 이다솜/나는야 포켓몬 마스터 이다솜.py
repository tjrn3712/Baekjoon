import sys
from collections import deque
import math
ipt = sys.stdin.readline

n, m = map(int, ipt().rstrip('\n').split())

pokemons = dict()
for i in range(n):
    pokemons[ipt().rstrip('\n')] = i
g = list(pokemons.keys())

for i in range(m):
    a = ipt().rstrip('\n')
    if not a.isdigit():
        print(pokemons[a] + 1)
    else:
        print(g[int(a) - 1])