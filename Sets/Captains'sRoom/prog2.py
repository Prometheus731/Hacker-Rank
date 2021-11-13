K = input()
roomList = input().split()
set1 = set()
set2 = set()
for i in roomList:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)
print(set1)
print(set2)
s3 = set1.difference(set2)
print(s3.pop())
