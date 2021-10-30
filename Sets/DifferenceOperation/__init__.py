if __name__ == '__main__':
    n = input()
    listN = set(input().split())
    b = input()
    listB = set(input().split())
    count = 0
    differenceSet = listN.difference(listB)
    for i in differenceSet:
        count += 1
    print(count)



