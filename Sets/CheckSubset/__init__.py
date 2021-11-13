if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        A = int(input())
        setA = set(input().split())
        B = int(input())
        setB = set(input().split())

        if setA.issubset(setB):
            print('True')
        else:
            print('False')
