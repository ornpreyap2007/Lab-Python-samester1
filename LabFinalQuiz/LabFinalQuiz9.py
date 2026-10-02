xo = []
for i in range(9) :
    x = input('Input: ')
    if x not in ["x","o"] :
        print('Wrong input')
        exit()
    xo.append(x)
print('-------') 
for j in range(0,9,3) :
    print(f"|{xo[j]}|{xo[j+1]}|{xo[j+2]}|\n-------")
    