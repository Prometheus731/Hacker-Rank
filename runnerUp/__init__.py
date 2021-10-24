if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # maxNum=max(arr)
    # for i in arr:
    #     if(i==maxNum):
    #         arr.remove(i)
    newList=[]
    for i in arr:
        if i not in newList:
            newList.append(i)

    newList.sort()
    newList.remove(max(newList))
    print(max(newList))