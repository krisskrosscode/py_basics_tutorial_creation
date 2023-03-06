import math

def area_of_circle():
    radius = float(input('Enter radius : '))
    return f"Area of the circle with radius {radius} is {math.pi*radius*radius} sq. units"

def area_of_triangle():
    base = float(input("Enter base length : "))
    height = float(input("Enter height : "))

    return f"Area if triangle with base {base} units and height {height} units is {0.5*base*height} sq. units"

def area_of_square():
    side = float(input("Enter side length : "))
    return f"Area of square with side length {side} is {side*side} sq. units"

def Menu():
    choice = int(input("Enter shape you want to find the area of \n1.Circle\n2.Triangle\n3.Square\n\n"))

    if choice ==1 :
        ans = area_of_circle()
    
    elif choice ==2 :
        ans = area_of_triangle()

    else :
        ans = area_of_square()

    return ans

if __name__=="__main__":
    ans = Menu()
    print(ans)