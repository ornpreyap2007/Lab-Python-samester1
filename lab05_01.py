e = 0
o = 0
for i in range(1,6) :
    n = int(input(f'enter a number '))
    if n%2 == 0 :
        e += 1
    else :
        o += 1
print(f'''there were {e} even numbers
there were {o} odd numbers''')
