a = sorted([[int(input()),i+1] for i in range(8)],reverse=1)
print(sum([i[0] for i in a][:5]))
print(*sorted([i[1] for i in a][:5]))