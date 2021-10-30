if __name__ == '__main__':
    n = input()
    listN = set(input().split())
    b = input()
    listB = set(input().split())
    count = 0
    symmetricDiffSet = listN.symmetric_difference(listB)
    for i in symmetricDiffSet:
        count += 1
    print(count)



