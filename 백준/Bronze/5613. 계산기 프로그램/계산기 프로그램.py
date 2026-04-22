result = int(input())

while True:
    operator = input()
    
    if operator == '=':
        print(result)
        break
    
    num = int(input())
    
    if operator == '+':
        result += num
    elif operator == '-':
        result -= num
    elif operator == '*':
        result *= num
    elif operator == '/':
        result //= num
