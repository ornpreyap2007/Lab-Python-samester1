def get_score(item):
    return item[1]
student_score = {}
while True :
    st_sc = input('Enter student name and score: ')
    if st_sc == "end 0" or st_sc == "end":
        break
    try :
        st,sc = st_sc.split()
    except ValueError :
        print('Invalid input')
        continue
    if not sc.isnumeric() :
        print('Invalid score!')
        continue
    sc = int(sc) 
    if not(0<=sc<=100) :
        print('Invalid score!')
        continue
    if st not in student_score :
        student_score[st] = sc
    else :
        print('Duplicate name!')
        continue
print('List:')
if len(student_score) == 0 :
    print('> empty list!')
    exit()
for key, value in sorted(student_score.items(), key=get_score,reverse=True):
    print(key, "\t", value)