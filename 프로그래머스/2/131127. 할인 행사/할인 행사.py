def solution(a, b, c):
    return sum(sum(c[i:i+10].count(a[j])!=b[j]for j in range(len(a)))==0 for i in range(len(c)-9))