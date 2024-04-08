from datetime import datetime

N, M, P = map(int, input().split())
ps = input().split()
ss = [input().split() for _ in range(P)]
sc = {p: 0 for p in ps}
at = {p: {str(i): [] for i in range(1, N+1)} for p in ps}

for pr, t, n, r in ss:
    at[n][pr].append((datetime.strptime(t, "%H:%M"), r))

for i in range(1, N+1):
    ps = []
    for p, prs in at.items():
        a = prs[str(i)]
        if not a: 
            sc[p] += M + 1
            continue
        f = s = None
        for t, r in a:
            if r == "wrong" and f is None: f = t
            elif r == "solve": s = t; break
        if s is None: 
            sc[p] += M
        elif f is None: 
            sc[p] += M + 1
        else: 
            ps.append((s - f, p))
    for r, (_, p) in enumerate(sorted(ps), 1): sc[p] += r

print('\n'.join(sorted(sc, key=lambda x: (sc[x], x))))
