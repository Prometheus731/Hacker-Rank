if __name__ == '__main__':
    listIndex = map(int, input().split())
    listArray = input().split()

    setA = set(input().split())
    setB = set(input().split())

    happiness = 0
    for i in listArray:
        if i in setA:
            happiness += 1
        if i in setB:
            happiness -= 1

    print(happiness)



