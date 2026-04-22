for _ in ' '*int(input()):
    a = ""
    b = "."
    while b:
        b = input()
        a += b
    print("Efficiency ratio is %g%%." % round(100*(1-a.count("#")/len(a)), 1))
