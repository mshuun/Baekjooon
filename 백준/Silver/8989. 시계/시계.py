for _ in range(int(input())):
    print(sorted((min(abs((h%12)*30+m*0.5-m*6),360-abs((h%12)*30+m*0.5-m*6)),f'{h:02d}:{m:02d}')for h,m in[map(int,t.split(':'))for t in input().split()])[2][1])