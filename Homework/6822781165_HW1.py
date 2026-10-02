import math as m

print('''Capsule Calculator
1. Volume
2. Surface Area''')
s = input('Select Calculation (1 or 2): ')
r = float(input('Enter radius (meters): '))
a = float(input('Enter side length (meters): '))

if s == "1" :
   volume = m.pi*m.pow(r,2)*((4/3)*r+a)
   print(f'Volume = {volume:.4f} cubic meters')
elif s == "2" :
   surface_area = 2*m.pi*r*(2*r+a)
   print(f'Surface Area = {surface_area:.4f} square meters')
else :
   print("Invalid selection. Cannot calculate.")