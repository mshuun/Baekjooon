N = int(input())
ns = [*map(int, input().split())]

arr = [[x, [x]] for x in ns]

def re(arr, target_n):
    if target_n == 1:
        return arr[0][1]
    
    new_arr = []
    odd = None
    evn = None
    
    for i in range(len(arr)):
        val = arr[i][0]
        ns = arr[i][1]
        
        if val % 2 == 0:
            if evn is None:
                evn = arr[i]
            else:
                new_n = (evn[0] + val) // 2
                new_ns = evn[1] + ns
                new_arr.append([new_n, new_ns])
                evn = None
        else:
            if odd is None:
                odd = arr[i]
            else:
                new_n = (odd[0] + val) // 2
                new_ns = odd[1] + ns
                new_arr.append([new_n, new_ns])
                odd = None

    return re(new_arr, target_n // 2)

ans = re(arr, N)
print(*ans)