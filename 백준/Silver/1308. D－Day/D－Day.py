from datetime import datetime

date1 = datetime(*map(int, input().split()))
date2 = datetime(*map(int, input().split()))

diff = (date2 - date1).days

if diff >= 365243:
    print("gg")
else:
    print(f"D-{diff}")
