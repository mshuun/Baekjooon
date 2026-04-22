n = int(input())
nums = list(map(int,input().split()))
result = 0
for i in range(n):
    if i+1 != nums[i]:
        result += 1
print(result)