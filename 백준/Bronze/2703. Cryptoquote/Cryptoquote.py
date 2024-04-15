T = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(T):
    cipher = input()
    re = input().lower()
    for i in range(26):
        cipher = cipher.replace(alphabet[i], re[i])
    print(cipher.upper())
