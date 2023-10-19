n, d = map(int, input().split())

for i in range(0, n) : 
    string = input()
    result = ''
    
    for j in range (0, n) : 
        
        if d == 1 : 
            if string[j] == 'd' : 
                result += 'q'
            elif string[j] == 'b' : 
                result += 'p'
            elif string[j] == 'q' : 
                result += 'd'
            elif string[j] == 'p' : 
                result += 'b'
        
        elif d == 2 : 
            if string[j] == 'd' : 
                result += 'b'
            elif string[j] == 'b' : 
                result += 'd'
            elif string[j] == 'q' : 
                result += 'p'
            elif string[j] == 'p' : 
                result += 'q'

    print(result)