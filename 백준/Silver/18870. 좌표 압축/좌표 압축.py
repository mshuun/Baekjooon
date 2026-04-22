n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(set(arr))
arr2_index = {num: index for index, num in enumerate(arr2)}
arr3 = [arr2_index[num] for num in arr]
print(*arr3)