print('''Menu:
===============
A - Americano (50)
E - Espresso (40)
G - Green tea (60)
''')
order = input("input = ")
quantity , total = 0 , 0
for x in order :
    if x == "A" :
        quantity += 1
        total += 50
        print(f'{quantity}. Americano 50')
    elif x == "E" :
        quantity += 1
        total += 40 
        print(f'{quantity}. Espresso 40')
    elif x == "G" :
        quantity += 1
        total += 60
        print(f'{quantity}. Green tea 60')
vat = total * 0.07
print(f'''Quantity: {quantity}
Vat: {vat:.2f}
Total: {total:.2f}
Grand total: {total + vat:.2f}''')