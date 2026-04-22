n = int(input())

for i in range(n):
    name = input()
    converted_name = ''
    for char in name:
        if char == 'Z':
            converted_name += 'A'
        else:
            converted_name += chr(ord(char) + 1)
    
    print(f"String #{i+1}")
    print(converted_name)

    if i < n - 1:
        print()
