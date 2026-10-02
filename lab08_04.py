St_sc = {}
while True :
    x = input('Input (DONE = exit): ')
    if x == "DONE" :
        break
    x= x.split()
    if len(x) != 2 :
        print('input must only have 2 values')
        continue
    a,b = x
    if len(a) != 10 or a.isalpha() :
        print('Student ID must be a number!')
        continue
    if not (b.isnumeric()) :
        print('score must be a number!')
        continue
    if a not in St_sc :
        St_sc[a] = b
    else :
        print('Duplicated ID')
print('Output:')
for key , values in St_sc.items() :
    print(key," ",values)

    

