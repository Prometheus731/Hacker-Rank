if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum = 0;
newList = []
newList1 = []
if (query_name in student_marks):
    newList.append(student_marks[query_name])

# print(newList)
newList1 = newList[0]
# print(newList1)


for i in newList1:
    sum = sum + i
avg = round((sum / 3), 2)
print('%.2f' % avg)
