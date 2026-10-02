d = int(input('Enter distance (km)= '))

if 0 <= d <100 :
    print(f'''The cost is 10 dollors.''')
elif 100 <= d < 150 :
    print(f'''The cost is {(10+5*(d-100)):.2f} dollors''')
elif 150 <= d :
    print(f'''The cost is {(260+7*(d-150)):.2f} dollors.''')
else :
    print('error')