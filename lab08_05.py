x = input('Input a sentence: ').split()
dict = {}
check = False
for i in x :
    i = i.lower()
    if i not in dict :
        dict[i] = 1
    else :
        dict[i] += 1
        check = True
print('Output:')
if check :
    for key,values in dict.items() :
        if values > 1 :
            print(key)
else :
    print('none')


