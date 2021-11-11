# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    K = int(input())
    roomListA = input().split()
    roomListB = []
    roomListC = []

    for i in range(0, len(roomListA)):
        if i < len(roomListA) // 2:
            roomListB.append(roomListA[i])
        else:
            roomListC.append(roomListA[i])
    setB = set(roomListB)
    setC = set(roomListC)
    diffA = setC.difference(setB)
    diffB = setB.difference(setC)

    if diffA:
        print(diffA.pop())
    else:
        print(diffB.pop())

