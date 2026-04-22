n, k = map(int, input().split())
a = list(map(int, input().split()))

sorted_a = sorted(a)
pos = {val: idx for idx, val in enumerate(a)}
cnt = 0

for last in range(n - 1, 0, -1):
    target = sorted_a[last]
    max_idx = pos[target]
    
    if max_idx != last:
        a[max_idx], a[last] = a[last], a[max_idx]
        
        pos[a[max_idx]] = max_idx
        pos[a[last]] = last
        
        cnt += 1
        if cnt == k:
            print(*(a))
            break
else:
    print(-1)