def octal_to_decimal(octal):
    decimal, i = 0, 0
    while(octal != 0):
        dec = octal % 10
        decimal = decimal + dec * pow(8, i)
        octal = octal//10
        i += 1
    return decimal



def decimal_to_binary(num):
    ans = ""
    if num == 0 :
        return 0
    while num:
        ans += str(num&1)
        num = num >> 1
     
    ans = ans[::-1]
 
    return ans

def octal_to_binary(num):
    ans = octal_to_decimal(num)
    ans = decimal_to_binary(ans)

    return ans

print(octal_to_binary(345))
