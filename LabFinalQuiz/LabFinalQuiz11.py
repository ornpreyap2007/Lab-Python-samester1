count_animals = {}
while True :
    x = input('Input: ')
    if x == "done" :
        break
    parts = x.split()
    if len(parts) != 2 :
        print('Error')
        continue
    animal , amount = parts
    try :
        amount = int(amount)
    except ValueError :
        print('Your second input must be number')
        continue
    if animal not in count_animals :
        count_animals[animal] = amount
    else :
        count_animals[animal] += amount
if len(count_animals) == 0 :
    print('Empty List')
    print('###Summary###')
    exit()
print('###Summary###')
for key , value in count_animals.items() :
    print(f'Total Number of {key} : {value}')



