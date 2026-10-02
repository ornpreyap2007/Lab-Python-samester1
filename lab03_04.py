import math as m


xp1 = int(input('Enter coordinate X for P1: '))
yp1 = int(input('Enter coordinate y for P1: '))
xp2 = int(input('Enter coordinate X for P2: '))
yp2 = int(input('Enter coordinate y for P2: '))

D = m.sqrt((m.pow((xp1-xp2),2))+(m.pow((yp1-yp2),2)))
R = D/2
A = m.pi*m.pow(R,2)
C = m.pi*D

print(f'''The length of the circle diameter is {D:.4f}''')
print(f'''The circle area and circumference are {A:.4f} and {C:.4f}''')