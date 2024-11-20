import random;l=list(range(1,20001));
for i in range(5):
    random.shuffle(l)
    print(*l)