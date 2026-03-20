import sys

input = sys.stdin.readline

n = int(input())
tanghulu = list(map(int, input().split()))

left = 0
max_fruit = 0
fruit_count = {}
kind_count = 0

for right in range(n):
    target = tanghulu[right]
    if target not in fruit_count or fruit_count[target] == 0:
        kind_count += 1
        fruit_count[target] = 1
    else:
        fruit_count[target] += 1

    while kind_count > 2:
        out_target = tanghulu[left]
        fruit_count[out_target] -= 1
        if fruit_count[out_target] == 0:
            kind_count -= 1
        left += 1
    max_fruit = max(max_fruit, right - left + 1)

print(max_fruit)
