for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        print(f"Case #{i+1}: equilateral")
    elif a + b <= c or b + c <= a or a + c <= b:
        print(f"Case #{i+1}: invalid!")
    elif a == b or b == c or a == c:
        print(f"Case #{i+1}: isosceles")
    else:
        print(f"Case #{i+1}: scalene")