from collections import Counter as c
input()
print(*[a for a,b in c([*map(int, input().split())]).most_common() for _ in range(b)])