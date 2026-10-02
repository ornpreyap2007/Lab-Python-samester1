import numpy as np
x = input('Input size of matrix: ')
if not x .isnumeric() :
    print('Invalid size!')
    exit()
x = int(x)
metrix = []
for i in range(x):
    row = []
    for j in range(x) :
        element = input(f'Input element at row {i+1} column {j+1}: ')
        element = float(element)
        row.append(element)
    metrix.append(row)
Metrix = np.array(metrix)
print('Output:')
print(f'Matrix =\n{Metrix}')
Determinant = np.linalg.det(Metrix)
if Determinant == 0 :
    print('This metrix can not be invert (determinant = 0).')
    exit()
Inverse = np.linalg.inv(Metrix)
print(f'Determinant = {Determinant}')
print(f'Inverse matrix =\n{Inverse}')





