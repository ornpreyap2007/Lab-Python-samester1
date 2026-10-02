from operator import itemgetter
programs={'ce':0,'che':0,'ec':0,'ie':0,'me':0}
score={}
while True:
    info=input('input: ').split()
    if info[0]=='done':
        break
    if info[1] in programs:
        programs[info[1]]+=1
    if 0<=float(info[2])<=4.00 and info[1] in programs:
        score[info[0],info[1]]=float(info[2])
    else:
        print('ERROR')
print('--------SUMMARY---------')
for key,value in programs.items():
    print(f'{key} = {value}')
print('-----LIST-----')
if len(score)==0:
    print('This list is empty.')
    exit()
for key,value in sorted(score.items(),key=itemgetter(1),reverse=True):
    print(f'{key[0]}  {key[1]}  {value:.2f}')