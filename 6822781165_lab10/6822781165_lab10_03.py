import numpy as np

data = np.loadtxt('grades.tsv', delimiter =None, dtype=str)
credits = ([3,2,1,3,3,3])
id = data[:,0]
gpa = data[:,1:]
gpa = gpa.astype(float)
gpa = np.sum(gpa*credits,axis=1)/ np.sum(credits)
print('%-15s%-4s'% ("student ID","GPA"))
for i in range(id.shape[0]):
    print("%-15s%-0.2f"%(id[i],gpa[i]))
