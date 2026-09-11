def solution(arr):
    arr.sort(reverse=1)
    for i in range(arr[0],-1,-1):
        if sum(1 for j in arr if j >= i) >= i :
            return i