print('Welcome to Income Tax Computation Program')
income = int(input('Please enter your income (THB): '))
if income > 0 :
    if 0 < income <= 15000 :
        tax = income*0
        net = income-tax
    elif 15001 < income <= 50000 : 
        tax = (15000*0)+((income-15000)*0.05)
        net = income-tax
    elif 50001 < income <= 100000 : 
        tax = (15000*0)+(35000*0.05)+((income-50000)*0.075)
        net = income-tax
    elif 100000 < income : 
        tax = (15000*0)+(35000*0.05)+(50000*0.075)+((income-100000)*0.0010)
        net = income-tax
    print(f'''Tax expense = {tax:.2f}
Your net income after tax = {net:.2f}''')
else :
    print('You are in debt!')
