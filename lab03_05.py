import math as m 

d = int(input('Enter the sphere diameter: '))
r = d/2
V = (m.pi/6)*m.pow(d,3)
A = 4*m.pi*m.pow(r,2)

print(f'''The length of the sphere radius is {r:.4f}
The sphere volume and the surface area are {V:.4f} and {A:.4f}.''')