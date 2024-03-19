K = int(input())
a, b = map(int, input().split())
if b>a:a,b=b,a
print(K*K-(a/2-b/2)**2)