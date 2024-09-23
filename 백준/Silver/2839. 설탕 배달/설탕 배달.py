import sys

n = int(sys.stdin.readline())

i = -1
a = n // 3

for j in range(a + 1):
    if (n - 3 * (a - j)) % 5 == 0:
        i = a - j + (n - 3 * (a - j)) // 5

print(i)