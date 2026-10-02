import math as m

s = int(input('Enter score = '))
if 100 >= s >= 0 :
   if 100 >= s >= 80 :
       print('You got A!')
   elif 80 > s >= 70 :
       print('You got B!')
   elif 70 > s >= 60 :
       print('You got C!')
   elif 60 > s >= 40 :
       print('You got D!')
   else :
       print('You got F!')
else :
   print('Error')
