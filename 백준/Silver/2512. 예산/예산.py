def binary_search(requests, M, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for req in requests:
            if req > mid:
                total += mid
            else:
                total += req
        if total > M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


N = int(input())
requests = list(map(int, input().split()))
M = int(input())

start = 0
end = max(requests)

print(binary_search(requests, M, start, end))