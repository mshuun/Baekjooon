while True:
    try:
        a, b = map(int, input().split())
        print(f"{round(a/b, 2):.2f}")
    except:
        break
