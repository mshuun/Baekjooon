n = int(input())
s = input()
for i in [".", "|", ":", "#"]:
    s = " ".join(s.split(i))
print(sum(int(x) for x in s.split()))
