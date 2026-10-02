fre1 = input('Input: ').split()
sequence = {x:fre1.count(x) for x in fre1 if x.isnumeric() }
for key ,values in sequence.items():
    if int(key) == values :
        output = 'good sequence'
    else :
        output = 'not good sequence'
        break
print('Output:',output)

