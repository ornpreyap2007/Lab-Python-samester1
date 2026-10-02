from math import *
x = input('Input a positive number: ')
if x.isalpha() :
    print('Wrong Input')
    exit()
x = float(x)
if x < 0 :
    print('Wrong Input')
    exit()
def CirArea(x) :
    CirArea = pi*(x**2)
    print('The area of the circle is %.2f'%CirArea)
def SqArea(x) :
    SqArea = x*x
    print('The area of the square is %.2f'%SqArea)
CirArea(x)
SqArea(x)