num = 45



# print(x + y)


# first_name = "pooja"
# last_name = 'madavi'


# # full_name = first_name + last_name

# # print("My first name is {} and my last name is {}".format(first_name, last_name))
# # print(f"My first name is {first_name} and my last name is {last_name}")


# int
# float decimal 
# str -> string
# double decimal 

x = 90
y = 4

# Arithmetic operators

# print(x+y)
# print(x-y)
# print(x//y) #int
# print(x/y) #float
# print(x%y) # remainder


# # Comparison operators

# print(x != y)


# # bitwise operator

# print(x and y) 
# print(x & y) ## bitwise and 
# print(0 | 1)
# print(~0)

# a = 3 ## 0000 0011 -> 0000 0001

# print(a>>1) 

# somtu = 15
# pooja = 19

# harshal = None 
# yeeshu = None
# if somtu and pooja:
#     print('both are good siblings')

# if harshal or pooja:
#     print('you are good imaginary siblings')

# print(harshal is not pooja)

# lst = [1,23,124,12,4,12] ## 
# tup = (12,34,25,1,415,15,1) 
# print(398147 not in lst)

# n = len(lst)
# m = len(tup)

# print(tup[0:6])
# print(lst[-1])

# ## tuples are immutable
# lst[0] = -1
# print(lst)

# tup[0] = 13423
# print(tup)

## dictionary or hashmap
## key: value pairs 


madavi = {
    "pooja" : 'good sibling' ,#str,
    'sontu' : 'smart sibling' #str 
}

## python treats everything as an object 


# print(madavi.keys(), madavi.values())

# print(madavi['pooja'] + " ",  madavi['sontu'])

# print(type(madavi['pooja']))


def pooja() -> None:
    print('POoja is a good girl')  ## no return value 


def pooja_returns():
    return 'Pooja returns this value'

pooja()
print(pooja_returns())

print(type(pooja_returns()))


def int_division(numerator, denominator):
    print(numerator//denominator)

(int_division(10,3))