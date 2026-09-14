def solution(A,B):
    A = sorted(A)
    B = sorted(B,reverse=1)
    return sum(A[i]*B[i] for i in range(len(A)))