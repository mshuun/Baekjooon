n = int(input())
a = list()
for _ in range(n):
    a.append(input())
for s in a:
    l = len(s)
    if s[l//2-1] == s[l//2]:
        print("Do-it")
    else:
        print("Do-it-Not")