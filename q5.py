def decimal_to_binary(num):
        if num >= 1:
            decimal_to_binary(num // 2)
        print( num % 2 , end='')


def binary_to_decimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)


decimal_to_binary(-3)
print()
binary_to_decimal(110)