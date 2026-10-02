study_program = {"ce":0,"che":0,"ec":0,"ie":0,"me":0}
name_program = {}
while True :
    program = input('input: ')
    if program == "done" :
        break
    parts =  program.split()
    if len(parts) != 3 :
        print('your input are not complete!')
        continue
    name , program , gpa = parts
    if program not in study_program:  
        print('ERROR1')
        continue
    try :
        gpa = float(gpa)
    except ValueError :
        print('ERROR2')
        continue
    if not(0.00 <= gpa <= 4.00 ) :
        print('ERROR3')
        continue
    study_program[program] += 1
    if name not in name_program :
        name_program[name] = program , gpa
    else :
        print('Duplicated name!')
        continue

print('----SUMMARY----')
for key , value in study_program.items() :
    print(key,"=",value)
if not(len(name_program) == 0) :
    print('----LIST----')
    for key , value in sorted(name_program.items() ,key=lambda item:item[1][1] , reverse=True) :
        major , grades = value
        print(key,major,grades)  