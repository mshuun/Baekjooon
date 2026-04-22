t = int(input())
n = int(input())
f = list(map(int,input().split()))
s = sum(f)
if(t>s):
    print("Padaeng_i Cry")
else:
    print("Padaeng_i Happy")