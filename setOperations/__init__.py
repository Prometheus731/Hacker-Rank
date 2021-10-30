n = int(input())
s = set(map(int, input().split()))
N = int(input())
listSet = []
for i in range(0, N):
    listSet.append(input().split())
for i in listSet:
    if i[0] == 'pop':
        s.pop()
    elif i[0] == 'remove':
        s.remove(int(i[1]))
    elif i[0] == 'discard':
        s.discard(int(i[1]))

print(sum(s))

