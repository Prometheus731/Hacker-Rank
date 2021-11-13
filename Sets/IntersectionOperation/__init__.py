if __name__ == '__main__':
    n = input()
    listN = set(input().split())
    b = input()
    listB = set(input().split())
    count = 0
    intersectionSet = listN.intersection(listB)
    for i in intersectionSet:
        count += 1
    print(count)



