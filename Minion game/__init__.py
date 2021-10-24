def minion_game(string):
    subListString=[]
    for i in range(0,len(string)+1):
        for j in range(1,len(string)+1):
            subListString.append(string[i:j])
    count=0
    while('' in subListString):
        subListString.remove('')
    setList=set(subListString)
    for i in setList:
        print(i,subListString.count(i))

    # print(string)
    print(subListString)
    print(setList)

if __name__ == '__main__':
    s = 'banana'
    minion_game(s)