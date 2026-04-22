caseNum = int(input())
for i in range(caseNum):
    schNum = int(input())
    topValue=0
    for j in range(schNum):
        schName,schValue = input().split()
        schValue = int(schValue)
        if topValue<schValue :
            schTop = schName
            topValue = schValue
    print(schTop)