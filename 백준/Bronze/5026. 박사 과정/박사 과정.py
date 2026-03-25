for _ in range(int(input())):
    c = input()
    if c == "P=NP":
        print("skipped")
    else:
        a,b = map(int,c.split("+"))
        print(a+b)