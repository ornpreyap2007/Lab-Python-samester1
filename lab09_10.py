from math import *
def SquareArea(x) :
    area = x*x
    print('The area of the square is %.2f' %area)

def CircleArea(r) :
    area = pi*r**2
    print('The area of the circle is %.2f' %area)

type = input('Do you want to find the area of a square (s) or a circle (c)?: ')
if type == "s" :
    x = input('Enter the lenght: ')
    if x.isnumeric() :
        x= int(x)
        SquareArea(x)
    else :
        print('Input must be a number!')
        exit()
elif type == "c" :
    r = input('Enter the radius: ')
    if r.isnumeric():
        r = int(r)
        CircleArea(r)
    else :
        print('Input must be a number!')
        exit()
else :
    print('Wrong Input')
    exit()
