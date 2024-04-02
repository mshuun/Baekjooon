while True:
    N = int(input())
    if N == 0:
        break

    students = []
    macs = 0
    for i in range(N):
        name, height = input().split()
        height = float(height)
        students.append([name, height])
        macs = max(height, macs)
    print(*[name for name, height in students if height == macs])
