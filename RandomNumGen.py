import random
NumberList = []
NewNumList = []
ctr = 0
while ctr <= 15:
    num = random.randint(0,15)
    if num not in NumberList:
        if num == 0:
            pos = ctr
        NumberList.append(num)
        ctr += 1
NumberList[pos] = " "
print(NumberList)

NewNumList.append(NumberList[0:4])
NewNumList.append(NumberList[4:8])
NewNumList.append(NumberList[8:12])
NewNumList.append(NumberList[12:])

print(NewNumList)







