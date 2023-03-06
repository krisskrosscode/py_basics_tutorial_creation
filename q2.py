def power(num, index):
    if num == 0 and index == 0:
        return -1 # undefined
    
    if index==0:
        return 1
    
    if num == 1 or num == 0 :
        return num
    
    return num*power(num, index-1)

print(power(5, 3))