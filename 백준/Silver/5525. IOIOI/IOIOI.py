n = int(input())
m = int(input())
s = input()
count = 0
i = 0
now = 0
all = 0
while i+2 < len(s):
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        count += 1
        i += 2
        now += 1
        if now >= n:
            all += 1
    else:
        i += 1
        now = 0
print(all)