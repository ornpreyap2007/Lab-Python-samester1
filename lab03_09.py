import math as m
 
c = float(input('Enter the width of the cube: '))
wc = float(input('Enter the width of the container: '))
hc = float(input('Enter the height of the container: '))
dc = float(input('Enter the depth of the container: '))

cc = c*c*c
C = wc*hc*dc

ans = int(C//cc)

print(f'''The number of cubes that can fit into the container is {ans}.''')


