total_L , total_S , total_H = 0 , 0 , 0

for x in range(0,10) :
    feeling = input('Feeling Like ("L"), Sad ("S"), and Heart("H")? ') 
    if feeling == "L" :
        total_L += 1
    elif feeling == "S" :
        total_S += 1
    elif feeling == "H" :
        total_H += 1
    else :
        print("Invalid input, accepts only (L/S/H).")
total_input = total_L + total_S + total_H
print(f'''============
Total is {total_input}
============
Like : {total_L} ({(total_L/total_input)*100:.2f}%)
Sad : {total_S} ({(total_S/total_input)*100:.2f}%)
Heart : {total_H} ({(total_H/total_input)*100:.2f}%)
''')