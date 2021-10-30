# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    countrySet = set()
    for i in range(0, N):
        countrySet.add(input())

    count = 0
    for i in countrySet:
        count += 1
    print(count)

