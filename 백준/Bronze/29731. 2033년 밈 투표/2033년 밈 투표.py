N=int(input())
P=[input() for _ in range(N)]
A=["Never gonna give you up","Never gonna let you down","Never gonna run around and desert you","Never gonna make you cry","Never gonna say goodbye","Never gonna tell a lie and hurt you","Never gonna stop"]
for p in P:
    if p not in A:
        print("Yes")
        break
else:
    print("No")
