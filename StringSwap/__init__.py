def swap_case(s):
    # for i in range(len(s)):
        # print(ord(s[i]))
        # if(ord(s[i])>=65 and ord(s[i])<=90):
        #     print(s[i].lower())
        # elif(ord(s[i])>=97 and ord(s[i])<=122):
        # #     print(s[i].upper())
        # if(s[i].isupper()):
        #     print(s[i].lower())
        #     #str[i].insert(i,s[i].lower())
        #     s.replace(s[i],s[i].lower())
        # elif(s[i].islower()):
        #     print(s[i].upper())
        #     #str[i].insert(i,s[i].upper())
        #     s.replace(s[i],s[i].upper())

    str=s.swapcase();
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)