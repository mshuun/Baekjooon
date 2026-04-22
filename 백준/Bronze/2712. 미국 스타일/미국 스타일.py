T = int(input())
for _ in range(T):
    value,unit = input().split()
    value = float(value)
    if unit == 'kg':
        print("%.4f lb" % (value*2.2046))
    elif unit == 'l':
        print("%.4f g" % (value*0.2642))
    elif unit == 'lb':
        print("%.4f kg" % (value*0.4536))
    elif unit == 'g':
        print("%.4f l" % (value*3.7854))
        