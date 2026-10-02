import numpy as np
listofelement = []
for i in range(1,13) :
    element = input(f'Input C{i}: ')
    try :
        element = float(element)
        listofelement.append(element)
    except ValueError :
        print('Your input must integer!')
        exit()
a = np.array([
    [listofelement[0], listofelement[1], listofelement[2]],
    [listofelement[4], listofelement[5], listofelement[6]],
    [listofelement[8], listofelement[9], listofelement[10]]
])
b = np.array([listofelement[3],listofelement[7],listofelement[11]])
if np.linalg.det(a) == 0 :
    print('Unable to find a solution')
    exit()
else :
    c = np.linalg.inv(a)
    ans = np.matmul(c,b)
    print(f'''\nSolution:
x = {ans[0]:.2f}
y = {ans[1]:.2f}
z = {ans[2]:.2f}''')


