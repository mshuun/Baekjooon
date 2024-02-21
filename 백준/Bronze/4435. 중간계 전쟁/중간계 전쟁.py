def battle(g, s):
    gs, ss = [1, 2, 3, 3, 4, 10], [1, 2, 2, 2, 3, 5, 10]
    gt, st = sum([g[i] * gs[i] for i in range(6)]), sum([s[j] * ss[j] for j in range(7)])
    return "Good triumphs over Evil" if gt > st else "Evil eradicates all trace of Good" if gt < st else "No victor on this battle field"

T = int(input())
for i in range(1, T + 1):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print(f"Battle {i}: {battle(g, s)}")
