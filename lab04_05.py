#input
amount = int(input("Please specify amount of money you would like to withdraw: "))

#output
print("We may give you:")
if amount>=500:  
    n500 = amount//500
    print(f'{n500} bill(s) of 500 bath')
    amount = amount%500
if amount>=100:
    n100 = amount//100
    print(f'{n100} bill(s) of 100 bath')
    amount = amount%100
if amount>=50:
    n50 = amount//50
    print(f'{n50} bill(s) of 50 bath')
    amount = amount%50
if amount>=2:
    n2 = amount//2
    print(f'{n2} coin(s) of 2 bath')
    amount = amount%2
if amount>=1:
    n1 = amount//1
    print(f'{n1} coin(s) of 1 bath')
    amount = amount%1