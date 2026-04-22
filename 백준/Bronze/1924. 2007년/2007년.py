import datetime
m, d = map(int, input().split())
a = datetime.date(2007, m, d).weekday()
b = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(b[a])