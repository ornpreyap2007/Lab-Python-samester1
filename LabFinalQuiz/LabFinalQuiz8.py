number = {}
while True :
    n = input('Input: ')
    if n == "done" :
        break
    try :
        n = int(n)
    except :
        print('Error')
        continue
    if not (1 <= n <= 1000) :
        print('Error')
        continue
    if n not in number :
        number[n] = 1
    else :
        number[n] += 1
print('----SUMMARY----')
if len(number) == 0 :
    print('The list is empty')
else :
    for key , value in sorted(number.items(),key=lambda x : x[0] ) :
        print(key,"",value)