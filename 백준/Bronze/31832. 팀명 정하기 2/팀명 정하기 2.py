n = int(input())
for _ in range(n):
    s = input()
    
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    cond1 = upper_count <= lower_count
    
    cond2 = len(s) <= 10
    
    cond3 = not s.isdigit()
    
    if cond1 and cond2 and cond3:
        print(s)
        break