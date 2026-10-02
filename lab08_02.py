sequence = {}
x = input('Input: ').split()
for i in x :
    if i.isnumeric() :
        if i not in sequence :
            sequence[i] = 1
        else :
            sequence[i] += 1
for key,values in sequence.items() :
    if int(key) != values :
        print('Output: not good sequence')
        exit()
print('Output: good sequence')


