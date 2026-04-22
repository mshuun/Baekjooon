k = int(input())
c = 25 + k*0.01
if c < 100:
    c = 100
elif c > 2000:
    c = 2000
print("%.2f" % c)