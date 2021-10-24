list1 = input().split()
N = int(list1[0])
M = int(list1[1])

mid = int(N / 2)
for i in range(1, N, 2):
    print((i * '.|.').center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N - 2, 0, -2):
    print((i * '.|.').center(M, '-'))
