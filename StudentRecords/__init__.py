if __name__ == '__main__':
    newList=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newList.append([name,score])

def customKey(newList):
    return newList[1]

newList.sort(key=customKey)
newList1=[]
minNUmber=newList[0]

for i in newList:
    if i[1]!=minNUmber[1]:
        newList1.append(i)

newList2=[]
minNumber=newList1[0]
for i in newList1:
    if i[1]==minNumber[1]:
        newList2.append(i[0])

newList2.sort()
for i in newList2:
    print(i)


