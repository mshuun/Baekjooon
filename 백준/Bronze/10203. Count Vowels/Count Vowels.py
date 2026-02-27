t = int(input())
vowels = set("aeiou")
for _ in range(t):
    w = input().strip()
    cnt = sum(c in vowels for c in w)
    print(f"The number of vowels in {w} is {cnt}.")