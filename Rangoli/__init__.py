import string


# def print_rangoli(size):
#     # your code goes here
#     # size1=size+(size-1)
#     # size2=size1+(size1-1)
#     # alphList=[]
#     # str1=""
#     #
#     # for i in range(1,size+1,1):
#     #     alphList.append(chr(96+i))
#     #
#     # alphList.reverse()
#     #
#     # print("-".join(alphList))
#     #
#     # for i in range(1,size1,2):
#     #     print((i*'%').center(size2,"-"))
#     #
#     # print("Anshu".center(size2,"*"))
#     # for i in range(size1-2,0,-2):
#     #     print((i*"@").center(size2,"-"))
#     #
#     # #alphList=[]
#     #
#     #
#     # print('-'.join(alphList),end="")
#     #
#     # alphList.pop(0)
#     # print('-',end="")
#     # print('-'.join(alphList))
#     #
#     alpha=string.ascii_lowercase
#     print("Alpha- ",alpha)
#
#     for i in range(0,size):
#         s="-".join(alpha[i:size])
#
#     print(s)
#
#


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



