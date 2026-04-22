n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    print(f"Scenario #{i+1}:")
    #check right triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("yes")
    else:
        print("no")
    print()