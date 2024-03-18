import sys
I = sys.stdin.readline
ii = lambda:map(int, I().split())
S1, S2 = ii()
sample, system = 1, 1
for _ in range(S1):
    a, b = ii()
    if a != b:
        sample = 0
for _ in range(S2):
    a, b = ii()
    if a != b:
        system = 0
if sample and system:
    print('Accepted')
elif sample:
    print('Why Wrong!!!')
else:
    print('Wrong Answer')