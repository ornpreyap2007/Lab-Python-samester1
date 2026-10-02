student_info = {}
while True :
    user_input = input('Enter student ID and score: ')
    if user_input == "done 0" :
        break
    try :
        id_score = user_input.split()
    except ValueError :
        print('Invalid input!')
        continue
    if len(id_score) != 2 :
        print('Invalid input!')
        continue
    id , score = id_score
    if not (id.isdigit() and len(id) == 4) :
        print('Invalid ID format!')
        continue
    if not score.isdigit() :
        print('Invalid score!')
        continue
    score = int(score)
    if not 0 <= score <= 100 :
        print('Invalid score!') 
        continue
    if id not in student_info :
        student_info[id] = score
    else :
        print('The ID is already recorded!')

if len(student_info) == 0 :
    print('List:\n> no score is recorded!')
    exit()
else :
    print('List:')
    
for key in sorted(student_info.keys()) :
    print(key,'',student_info[key])
number_student = len(student_info)
average_score = sum(student_info.values())/len(student_info)
print(f'There are {number_student} student(s). The average score is {average_score:.2f} points.')




