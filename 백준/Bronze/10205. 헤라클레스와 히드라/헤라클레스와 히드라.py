for i in range(int(input())):
    head = int(input())
    cut = input()
    print(f"Data Set {i+1}:")
    print(head - cut.count('b') + cut.count('c'))
    print()
