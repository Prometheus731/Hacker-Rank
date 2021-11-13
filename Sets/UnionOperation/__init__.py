if __name__ == '__main__':
    n = input()
    listN = set(input().split())
    b = input()
    listB = set(input().split())
    count = 0
    unionSet = listN.union(listB)
    for i in unionSet:
        count += 1
    print(count)



