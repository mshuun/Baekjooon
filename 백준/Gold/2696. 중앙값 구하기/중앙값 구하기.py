t = int(input())
for _ in range(t):
    m = int(input())
    lst = []
    for _ in range((m-1)//10+1):
        lst.extend(map(int, input().split()))

    print(m//2+1)
    for j in range(0, m, 2):
        sorted_list = sorted(lst[:j+1])
        med = sorted_list[j//2]
        if j % 20 == 0 and j != 0:
            print()
        print(med, end=' ')
    print()
