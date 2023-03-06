from functools import reduce
 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiply_nums(lst):
    return reduce((lambda x, y: x * y), lst)
 
print(multiply_nums(lst))