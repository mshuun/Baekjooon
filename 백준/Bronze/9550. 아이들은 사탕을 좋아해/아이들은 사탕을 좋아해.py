T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    attendees = 0
    
    for candy in candies:
        attendees += candy // K
    
    print(attendees)
