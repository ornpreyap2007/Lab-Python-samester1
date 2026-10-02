print('''Welcome to pizza online ordering.
please input "y" if you want to order, otherwise input "n" ''')
price = 0

pz = input('pizza? (price_359) : ')
if pz == "y" : 
    price += 359
c = input('chicken? (price_3 pieces for 199) : ')
if c == "y" : 
    price += 199
pa = input('pasta? (price_99) : ')
if pa == "y" :
    price += 99
s= input('salad? (price_99) : ')
if s == "y" :
    price += 99
co = input('coke? (price_550 ml for 25) : ')
if co == "y" :
    price += 25

print(f'''total price is {price}
thanks''')