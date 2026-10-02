from math import *
def myCylinder(r,h):
    v = pi*(r**2)*h
    a = (2*pi*r*h)+(2*pi*(r**2))
    print('The volume is %.2f and the sur face area is %.2f'%(v,a))
r = input('Enter the redius of the cylinder : ')
h = input('Enter the height of the cylinder : ')
if r.isalpha() or h.isalpha() :
    print('Input must be a number!')
    exit()
else :
    r,h= float(r),float(h)
myCylinder(r,h)