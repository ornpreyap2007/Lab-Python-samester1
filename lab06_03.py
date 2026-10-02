n = []
ans = 0
print("="*20)
for i in range(5) :
    x = input(f'Input#{i+1}: ')
    if x.isalpha() :
        print('Please enter number!')
        exit()
    n.append(int(x))
select = input('Select the option: 1)Summary,2)average,3)min,4)max...')
if select == "1" :
    ans = sum(n)
elif select == "2" :
    ans = (sum(n)/5)
elif select == "3" :
    ans = min(n)
elif select == "4" :
    ans = max(n)
else :
    print('Please enter option correctly!')
print('Your result is',ans)
    

