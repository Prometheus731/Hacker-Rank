if __name__ == '__main__':
    n = input()
    setA = set(input().split())
    N = int(input())
    sum = 0
    for i in range(N):
        inputOperation = input().split()
        setB = set(input().split())
        if inputOperation[0] == 'intersection_update':
            setA.intersection_update(setB)
        elif inputOperation[0] == 'difference_update':
            setA.difference_update(setB)
        elif inputOperation[0] == 'symmetric_difference_update':
            setA.symmetric_difference_update(setB)
        else:
            setA.update(setB)

    for i in setA:
        sum += int(i)
    print(sum)
