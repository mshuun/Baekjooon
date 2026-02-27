n = int(input())
ok = True
for _ in range(n):
    if int(input()) < 48:
        ok = False
print("True" if ok else "False")