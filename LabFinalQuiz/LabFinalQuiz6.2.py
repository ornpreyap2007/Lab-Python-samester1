from operator import itemgetter
student_score = []
while True :
    inputtt = input('Enter student ID and score: ')
    if inputtt == "done 0" :
        break
    parts = inputtt.split()
    if len(parts) != 2 :
        print('Invalid ID format!')
        continue
    student , score = parts
    try :
        score = int(score) 
    except :
        print('Invalid score!')
        continue
    if not(0 <= score <= 100) :
        print('Invalid score!')
        continue
    if not(len(student) == 4 and student.isnumeric()):
        print('Invalid ID format!')
        continue
    if any(student == item[0] for item in student_score ):
        print('The ID is already recorded!')
        continue
    else :
        student_score.append((student,score))
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

     

