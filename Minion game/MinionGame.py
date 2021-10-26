def minion_game(string):
    countVowel = 0
    countConsonant = 0
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            countVowel += (len(string) - i)
        else:
            countConsonant += (len(string) - i)

    if countVowel > countConsonant:
        print("Kevin", countVowel)
    elif countVowel < countConsonant:
        print("Stuart", countConsonant)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
