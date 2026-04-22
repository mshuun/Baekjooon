a=int(input())
for i in range(a):
    b=i
    for j in range(len(str(i))):
        b += int(str(i)[j])
    if b == a :
        print(i)
        break
    if i == a-1 :
        print(0)
