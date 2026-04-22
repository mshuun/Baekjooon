a,b,c = map(int,input().split())
x,y,z = map(int,input().split())
grade = 'E'
if x>=a and y>=b and z>=c:
    grade = 'A'
elif x>=a/2 and y>=b and z>=c:
    grade = 'B'
elif y>=b and z>=c:
    grade = 'C'
elif y>=b/2 and z>=c:
    grade = 'D'
print(grade)
