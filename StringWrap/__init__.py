import textwrap
str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
width=4
# print(str)
# str1=list(str)
# print(str1)
# x=width
# j=1
# for i in range(0,len(str1)):
#     if(i==width):
#         print(i)
#         str1.insert((i),'\n')
#         j+=1
#         width=x
#         width=width*j
#
# print((('').join(str1)))
print(textwrap.fill(str,width))