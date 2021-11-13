if __name__ == '__main__':
    setA = set(input().split())
    n = int(input())
    setBoolean = set()
    for i in range(n):
        setB = set(input().split())

        if setB.issubset(setA):
            setBoolean.add('True')
        else:
            setBoolean.add('False')
    flag = 0
    for j in setBoolean:
        if j == 'False':
            flag = 1

    if flag == 1:
        print('False')
    else:
        print('True')
