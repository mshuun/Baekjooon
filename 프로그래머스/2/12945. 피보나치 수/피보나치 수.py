def solution(n):
    a = [0,1,1]
    for i in range(2,n):
        a.append(a[i]+a[i-1])
    return a[n]%1234567