N = int(input())
K = input()
B = K.count('B')
S = K.count('S')
A = K.count('A')
if A == S == B:
    print('SCU')
elif B > S and B > A:
    print('B')
elif S > B and S > A:
    print('S')
elif A > B and A > S:
    print('A')
elif S == B:
    print('BS')
elif S == A:
    print('SA')
else:
    print('BA')