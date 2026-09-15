def solution(routes):
    routes.sort(key=lambda x: x[1])
    n = len(routes)
    cam = [routes[0][1]]
    
    for car in routes:
        a,b = car
        c = 0
        if a <= cam[-1] <= b:
            continue
        else:
            cam.append(b)
    return len(cam)