inp = list(input())
for i in range(len(inp)):
    if inp[i] == 'A' or inp[i] == 'B' or inp[i] == 'C':
        inp[i] = 2
    elif inp[i] == 'D' or inp[i] == 'E' or inp[i] == 'F':
        inp[i] = 3
    elif inp[i] == 'G' or inp[i] == 'H' or inp[i] == 'I':
        inp[i] = 4
    elif inp[i] == 'J' or inp[i] == 'K' or inp[i] == 'L':
        inp[i] = 5
    elif inp[i] == 'M' or inp[i] == 'N' or inp[i] == 'O':
        inp[i] = 6
    elif inp[i] == 'P' or inp[i] == 'Q' or inp[i] == 'R' or inp[i] == 'S':
        inp[i] = 7
    elif inp[i] == 'T' or inp[i] == 'U' or inp[i] == 'V':
        inp[i] = 8
    elif inp[i] == 'W' or inp[i] == 'X' or inp[i] == 'Y' or inp[i] == 'Z':
        inp[i] = 9
print(sum(inp)+len(inp))