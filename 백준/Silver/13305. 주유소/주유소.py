n = int(input())
road = [0]
t = list(map(int, input().split()))
road.extend(t)
price = list(map(int, input().split()))
money = 0
now = 0
nowPrice = price[now]
destination = 1
while now != n:
    try:
        while price[destination] >= nowPrice:
            destination += 1
    except:
        if destination == n:
            money += nowPrice*sum(road[now+1:n])
        break
    money += nowPrice*sum(road[now+1:destination+1])
    now = destination
    nowPrice = price[now]
    destination += 1

print(money)
