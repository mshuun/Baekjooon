from math import factorial as f
import sys
input = sys.stdin.readline
while(n:=int(input())):
 r=i=0
 while n:r+=f(i:=i+1)*(n%10);n//=10
 print(r)
