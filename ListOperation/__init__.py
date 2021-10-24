if __name__ == '__main__':
    N = int(input())
    newList = []
    for i in range(N):
        newList.append(input().split())
    list1 = []
    for i in newList:
        if (i[0] == "insert"):
            list1.insert(int(i[1]), int(i[2]))
        elif (i[0] == 'print'):
            print(list1)
        elif (i[0] == 'remove'):
            list1.remove(int(i[1]))
        elif (i[0] == 'append'):
            list1.append(int(i[1]))
        elif (i[0] == 'sort'):
            list1.sort()
        elif (i[0] == 'pop'):
            list1.pop()
        elif (i[0] == 'reverse'):
            list1.reverse()


