import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    out = []
    match = {')': '(', ']': '['}
    
    for line in lines:
        if line == '.':
            break
        
        stack = []
        is_valid = True
        
        for c in line:
            if c in "([":
                stack.append(c)
            elif c in ")]":
                if not stack or stack.pop() != match[c]:
                    is_valid = False
                    break
        
        if is_valid and not stack:
            out.append("yes")
        else:
            out.append("no")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()