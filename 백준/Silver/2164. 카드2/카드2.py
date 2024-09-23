import sys
from collections import deque

cards = deque(range(1, int(sys.stdin.readline()) + 1))

while len(cards) != 1:
    cards.popleft()
    a = cards.popleft()
    cards.append(a)

print(cards[0])