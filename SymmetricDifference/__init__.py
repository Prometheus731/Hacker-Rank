# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    M = input()
    listM = input().split()
    N = input()
    listN = input().split()
    interSection = set(listM).intersection(set(listN))
    interSection = list(map(int,interSection))
    # listM = listM.sort()
    # listN = listN.sort()
    # for i in listM:
    #     if i not in interSection:
    #         print(i)
    #
    # for j in listN:
    #     if j not in interSection:
    #         print(j)
    unionList = list(set(listM).union(set(listN)))
    unionList = list(map(int, unionList))
    # print(unionList)
    unionList.sort()
    # print(unionList)
    for i in unionList:
        if i not in interSection:
            print(i)
