charge = int(input('Input parking time (in minutes): '))
if charge >= 60 :
    cost = (charge//60)*20
    charge = charge%60
if charge > 15 :
    cost += 20
print(f'The charge is {cost} baht.')