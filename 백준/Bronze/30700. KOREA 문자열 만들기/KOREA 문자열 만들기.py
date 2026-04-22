a = input()
k = ["K", "O", "R", "E", "A"]
i = 0
r = 0
for c in a:
    if c == k[i % 5]:
        r += 1
        i += 1
print(r)
