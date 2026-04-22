k = int(input())

for dataset in range(1, k + 1):
    n, s, d = map(int, input().split())
    total_repayment = 0

    for _ in range(n):
        di, vi = map(int, input().split())
        time_required = di / s
        if time_required <= d:
            total_repayment += vi

    print("Data Set {}:".format(dataset))
    print(total_repayment)
    print()