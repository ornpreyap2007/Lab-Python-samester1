name_score = {}
def get_score(item) :
    return item[1]
while True :
    x = input('Input: ')
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
else :
    sorted_player = sorted(name_score.items() , key=lambda x: x[1], reverse=True)
    average =  sum(name_score.values())/len(name_score)
    heighest = sorted_player[0][1]
    for name , score in sorted_player :
        medal = ""
        if  score == heighest :
            medal = "Gold"
        elif score > average :
            medal = "Silver"
        if medal :
            print(f'{name}\t{score}\t{medal}')
        else :
            print(f'{name}\t{score}')

