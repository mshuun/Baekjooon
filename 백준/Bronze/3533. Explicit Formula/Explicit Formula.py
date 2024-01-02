from itertools import combinations

input_list = list(map(int, input().split()))

result = False

for r in range(2, 4):
    for combo in combinations(input_list, r):
        combo_result = any(combo)
        result = result != combo_result

print(int(result))
