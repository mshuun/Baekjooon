from math import ceil

T = int(input())
for i in range(T):
    s, mom, dad = input().split()
    mom = mom.split("'")
    mom = int(mom[0])*12 + int(mom[1][:-1])
    dad = dad.split("'")
    dad = int(dad[0])*12 + int(dad[1][:-1])
    result = (dad + mom + (5 if s == 'B' else -5)) / 2
    a = result - 4
    b = result + 4
    a_foot = int(a // 12)
    a_inch = ceil(a % 12)
    if a_inch == 12:
        a_foot += 1
        a_inch = 0
    b_foot = int(b // 12)
    b_inch = int(b % 12)
    print(f"Case #{i+1}: {a_foot}'{a_inch}\" to {b_foot}'{b_inch}\"")
