x = input('Input a string: ')
consonants = [ i for i in x if (i.lower() not in "aeiou") and (i.isalpha())]
vowels = [i for i in x if i.lower() in "aeiou"]
print('The number of consonants =',len(consonants),'\nThe number of vowels =',len(vowels))
