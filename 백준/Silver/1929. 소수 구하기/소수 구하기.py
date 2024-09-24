import sys
from collections import deque
import math

n, m = map(int, sys.stdin.readline().rstrip('\n').split())
ran = list(range(n, m + 1))

primes = dict()
for i in range(1000001):
    primes[i] = 1
primes[0], primes[1] = 0, 0

for i in range(2, m + 1):
    if primes[i]:
        for j in range(2, m // i + 1):
            primes[i * j] = 0

for i in ran:
    if primes[i]:
        print(i)

