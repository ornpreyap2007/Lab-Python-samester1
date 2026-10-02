x = input('Input: ').lower().split()
grop = {}
for words in x :
    if words not in grop :
        grop[words] = 1
    else :
        grop[words] += 1
heighest = max(grop.values())
print('Output: ')
for key in grop:
    if grop[key] == heighest :
        print(key,"=",grop[key])