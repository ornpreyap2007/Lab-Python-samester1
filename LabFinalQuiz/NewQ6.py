from operator import itemgetter
student_score = []
while True :
    st_sc = input('Enter student ID and score:')
    if st_sc == "done 0" :
        break 
    try :
        st,sc = st_sc.split()
    except :
        print('Invalid ID format!')
        continue
    if not(st.isnumeric() and len(st) == 4 ):
        print('Invalid ID format!')
        continue
    try :
        if not(0 <=int(sc) <= 100 ):
            print('Invalid score!')
            continue
    except :
        print('Invalid score!')
        continue
    sc = int(sc)
    if any(st == item[0] for item in student_score ):
        print('The ID is already recorded!')
        continue
    else :
        student_score.append((st,sc))
print('List :')
if len(student_score) == 0 :
    print('> no score is recorded!')
    exit()
for st , sc in sorted(student_score,key=itemgetter(0)) :
    print(st," ",sc)
n_student = len(student_score)
scores = [s[1] for s in student_score]
average_score = sum(scores) / n_student
print(f'There are {n_student} student(s). The average score is {average_score:.2f} points.')



    