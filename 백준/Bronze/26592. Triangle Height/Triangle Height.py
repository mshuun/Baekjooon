for _ in range(int(input())):
    a,b = map(float,input().split())
    print("The height of the triangle is {:.2f} units".format(round(2*a/b,2)))