import math

n = 0

while True:
    d, r, t = map(float, input().split())
    
    if r == 0:
        break
    
    c = d * math.pi
    distance = (c * r) / (12 * 5280)
    speed = distance / (t / 3600)
    
    n += 1
    
    print(f"Trip #{n}: {distance:.2f} {speed:.2f}")
