def left_rotated(n,x) :
    return x[n:] + x[:n]
def reight_rotated(n,x) :
    return x[-n:] + x[:-n]
x = input('Enter 5 inputs: ').split()
n = input('Enter an integer number of rotation (0-4): ')
if not n.isnumeric() :
    print('Error!')
    exit()
n = int(n)
if not (0 <= n <= 4) :
    print('Error!')
    exit()
print('The left-rotation list :',left_rotated(n,x))
print('The right-rotation list :',reight_rotated(n,x))