n = int(input())
d = {}
for _ in range(n):
    w = input()
    d.setdefault(len(w), []).append(w)
for l in sorted(d):
    print("\n".join(sorted(set(d[l]))))