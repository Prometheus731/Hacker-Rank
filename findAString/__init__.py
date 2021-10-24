def count_substring(string, sub_string):
    countSub = 0
    j = 0
    for i in range(0, len(string)):
        str1 = string[i:(len(sub_string) + j)]
        j += 1
        if str1 == sub_string:
            countSub += 1
    return countSub

#To find the number of substring withing the string
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
