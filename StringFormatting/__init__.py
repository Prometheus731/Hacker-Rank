def print_formatted(number):
    lenBin=len(str(bin(number).replace('0b','')))
    for i in range(1,number+1):
        decNo=str(i)
        octNo=str(oct(i).replace('0o',''))
        hexno=str(hex(i).replace('0x',''))
        binNo=str(bin(i).replace('0b',''))

        #lenOct=len(str(oct(number+1).replace('0o','')))

        print(decNo.rjust(lenBin,' '),octNo.rjust(lenBin,' '),hexno.upper().rjust(lenBin,' '),binNo.rjust(lenBin,' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)