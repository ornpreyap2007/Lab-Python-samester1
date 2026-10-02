student_score = {}
while True :
    id_score = input('Enter student ID and score: ')
    if id_score == "done 0" :
        break
    parts = id_score.split()
    if len(parts) != 2 :
        print('Invalid Input!')
        continue
    id , score = parts
    try :
        score = int(score)
    except :
        print('Invalid score!')
        continue
    if not(0 <= score <= 100) :
        print('Invalid score!')
        continue
    if not id.isnumeric() :
        print('Invalid ID format!')
        continue
    if not len(id) == 4 :
        print('Invalid ID format!')
        continue
    if id not in student_score :
        student_score[id] = score
    else :
        print('The ID is already recorded!')
if len(student_score) == 0 :
    print('> no score is recorded!')
    exit()
print('List:')
for id in sorted(student_score.keys()) :
    print(id," ",student_score[id])
n_student = len(student_score)
average = sum(student_score.values())/len(student_score)
print(f'There are {n_student} student(s). The average score is {average:.2f} points.')
