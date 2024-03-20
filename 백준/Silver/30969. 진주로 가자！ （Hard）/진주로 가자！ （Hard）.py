import sys
input = sys.stdin.readline
cost_list = [0 for _ in range(1002)]
jinju_cost = 0
for _ in range(int(input())):
    destination, cost = input().split()
    cost = int(cost)
    if cost > 1000:
        cost_list[1001] += 1
    elif destination == 'jinju':
        jinju_cost = cost
    else:
        cost_list[cost] += 1
print(jinju_cost)
print(sum(cost_list[jinju_cost+1:]))
