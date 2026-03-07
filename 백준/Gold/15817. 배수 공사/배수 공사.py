import sys
input = sys.stdin.readline

N, x = map(int, input().split())
pipe = [[*map(int, input().split())] for _ in range(N)]

result = [0] * (x + 1)
result[0] = 1

for length_pipe, max_pipe in pipe:
    for length in range(x, -1, -1):
        
        if result[length] == 0:
            continue
            
        for use_count in range(1, max_pipe + 1):
            new_length = length + (use_count * length_pipe)
            
            if new_length <= x:
                result[new_length] += result[length]
            else:
                break

print(result[x])