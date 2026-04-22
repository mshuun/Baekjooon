from collections import deque
for _ in range(int(input())):
    N, M = map(int, input().split())
    doc = deque(map(int, input().split()))
    doc[M] = str(doc[M])
    printed = 0
    while doc:
        now = doc[0]
        istarget = isinstance(now, str)
        now = int(now)
        top = max(list(map(int, doc)))
        if now < top:
            doc.append(doc.popleft())
        else:
            doc.popleft()
            printed += 1
            if istarget:
                break
    print(printed)
