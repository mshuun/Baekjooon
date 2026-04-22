x,y = map(int,input().split())
original = []
new = []
for i in range(x):
    original.extend(list(input()))
input()
for i in range(x):
    new.extend(list(input()))
count = 0
for i in range(len(original)):
    if original[i] == new[i]:
        count += 1
print(count)