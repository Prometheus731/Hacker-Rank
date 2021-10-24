
def palindrome(number):
    reverse = 0
    number1 = number

    while number != 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if number1 == reverse:
        print(number1, "is palindrome")
    else:
        print(number1, "is not palindrome")


if __name__ == '__main__':
    print("Program to check whether a number is palindrome or not: ")
    palindrome(int(input("Enter a number: ")))
