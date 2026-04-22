n = int(input())
stu = [input().strip() for _ in range(n)]
ans = [input().strip() for _ in range(n)]
print(sum(a == b for a, b in zip(stu, ans)))