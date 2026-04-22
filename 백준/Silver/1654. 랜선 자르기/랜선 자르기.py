def binary_search(target, lans, start, end):
    low = start
    high = end
    while low <= high:
        mid = (low + high) // 2
        maxi = 0
        for lan in lans:
            maxi += lan//mid
        if target > maxi:
            high = mid - 1
        else:
            low = mid + 1
    return high


N, K = map(int, input().split())
lan = [int(input()) for _ in range(N)]
print(binary_search(K, lan, 1, max(lan)))
