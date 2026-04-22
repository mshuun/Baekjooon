N = input()
result = 0
for i in range(int(N)):
    n = str(i+1)
    three = n.count('3')
    six = n.count('6')
    nine = n.count('9')
    result += three + six + nine
print(result)