# code is working but not recommended for large value of string
def minion_game(string):
    subListString = []
    countVowel = 0
    countConsonant = 0
    for i in range(0, len(string) + 1):
        for j in range(1, len(string) + 1):
            subListString.append(string[i:j])
            if '' in subListString:
                subListString.remove('')


    # countVowel = 0
    # countConsonant = 0

    setList = set(subListString)
    for i in setList:
        if i[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            countVowel = countVowel + subListString.count(i)
        else:
            countConsonant = countConsonant + subListString.count(i)

    if countVowel > countConsonant:
        print("Kevin", countVowel)
    elif countVowel < countConsonant:
        print("Stuart", countConsonant)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
