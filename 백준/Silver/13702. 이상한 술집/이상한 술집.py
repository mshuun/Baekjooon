def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            total += x // mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


N, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))
start = 1
end = max(array)

print(binary_search(array, K, start, end))
