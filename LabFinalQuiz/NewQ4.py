name_score = {}
from operator import itemgetter
while True :
    x = input('Input:')
    if x == "done" :
        break
    parts = x.split()
    if len(parts) != 2 :
        print('Invalid input')
        continue
    name , score = parts
    try :
        score = int(score)
    except ValueError :
        print('Invalid input')
        continue
    if score <= 0 :
        print('Invalid input')
        continue
    if name not in name_score :
        name_score[name] = score
    else :
        print('Duplicated player')
if len(name_score) == 0 :
    print('No players')
    exit()
sorted_player = sorted(name_score.items() , key=itemgetter(1),reverse=True)
average = sum(name_score.values())/len(name_score)
highest = sorted_player[0][1]
for key , value in sorted_player :
    medel = ""
    if value == highest :
        medel = "Gold"
    elif value > average :
        medel = "Silver" 
    if medel :
        print(key,"\t",value,"\t",medel)
    else :
        print(key,"\t",value)

        