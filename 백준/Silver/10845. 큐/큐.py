import sys
from collections import deque


def push(deq, item):
    deq.append(item)


def pop(deq):
    if len(deq) == 0:
        print(-1)
    else:
        print(deq.popleft())


def size(deq):
    print(len(deq))


def empty(deq):
    if len(deq) == 0:
        print(1)
    else:
        print(0)


def front(deq):
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[0])


def back(deq):
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[-1])


deq = deque()
for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip('\n')

    if a == 'pop':
        pop(deq)
    elif a == 'size':
        size(deq)
    elif a == 'empty':
        empty(deq)
    elif a == 'front':
        front(deq)
    elif a == 'back':
        back(deq)
    elif 'push' in a:
        push(deq, a.split()[1])
