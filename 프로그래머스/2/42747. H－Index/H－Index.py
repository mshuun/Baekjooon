def solution(arr):
    for i in range(10000,-1,-1):
        if sum(1 for j in arr if j >= i) >= i :
            return i