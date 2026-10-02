seq1 = input('Input sequence1: ').split()
seq2 = input('Input sequence2: ').split()
seq1 = {x for x in seq1 if x.isnumeric()}
seq2 = {x for x in seq2 if x.isnumeric()}
if seq2 <= seq1 :
    print('Output: same set')
else :
    print('Output: differant set')