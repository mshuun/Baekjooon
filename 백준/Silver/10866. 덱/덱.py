import sys
deq = []
n = int(sys.stdin.readline())
def push_front(num):
    deq.insert(0,num)
def push_back(num):
    deq.append(num)
def pop_front():
    if len(deq)>0:
        a = deq[0]
        del deq[0]
        sys.stdout.write(str(a))
    else :
        sys.stdout.write(str(-1))
def pop_back():
    if len(deq)>0:
        a = deq[-1]
        del deq[-1]
        sys.stdout.write(str(a))
    else :
        sys.stdout.write(str(-1))
def size():
    sys.stdout.write(str(len(deq)))
def empty():
    if len(deq) > 0 :
        sys.stdout.write(str(0))
    else :
        sys.stdout.write(str(1))
def front():
    if len(deq) > 0 :
        sys.stdout.write(str(deq[0]))
    else :
        sys.stdout.write(str(-1))
def back():
    if len(deq) > 0 :
        sys.stdout.write(str(deq[-1]))
    else :
        sys.stdout.write(str(-1))

for i in range(n):
    do = list(sys.stdin.readline().split())
    if len(do) == 1 :
        f = do[0]
        if f == 'pop_front' :
            pop_front()
            sys.stdout.write('\n')
        elif f == 'pop_back' :
            pop_back()
            sys.stdout.write('\n')
        elif f == 'size' :
            size()
            sys.stdout.write('\n')
        elif f == 'empty' :
            empty()
            sys.stdout.write('\n')
        elif f == 'front':
            front()
            sys.stdout.write('\n')
        else :
            back()
            sys.stdout.write('\n')
    else :
        f = do[0]
        m = do[1]
        if f == 'push_front':
            push_front(m)
        else : push_back(m)
    