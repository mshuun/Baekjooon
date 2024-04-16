from math import ceil
for i in range(int(input())):
 s,m,d=input().split();m=int(m[0])*12+int(m[2:-1]);d=int(d[0])*12+int(d[2:-1]);r=(d+m+(5 if s=='B' else -5))/2;a=r-4;b=r+4;a_f=int(a//12);a_i=ceil(a%12);b_f=int(b//12);b_i=int(b%12);a_f,a_i=(a_f+1,0)if a_i==12 else(a_f,a_i);print(f"Case #{i+1}: {a_f}'{a_i}\" to {b_f}'{b_i}\"")
