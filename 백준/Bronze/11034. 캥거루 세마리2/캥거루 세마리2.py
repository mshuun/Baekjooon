while True:
    try:
        jump = 0
        a,b,c = map(int, input().split())
        while True:
            if a+2 == b+1 == c:
                break
            ab = b - a
            bc = c - b
            if ab > bc:
                c = b - 1
                c,b = b,c
                jump += 1
            else:
                a = b + 1
                a,b = b,a
                jump += 1
        
        print(jump)
            
    except:
        break