from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
q = deque()
def push(x): 
    q.append(x)
def pop():
    try : print(q.popleft())
    except : print('-1')
def size():
    print(str(len(q)))
def empty():
    if len(q) == 0 :
        print('1')
    else : print('0')
def front():
    try : print(str(q[0]))
    except :print('-1')
def back():
    try : print(str(q[-1]))
    except :print('-1')

for i in range(n):
    do = list(sys.stdin.readline().split())
    if len(do) == 1 :
        f = do[0]
        if f == 'pop' :
            pop()
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
        push(do[1])