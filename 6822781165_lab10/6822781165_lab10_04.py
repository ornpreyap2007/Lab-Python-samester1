import numpy as np
data = np.loadtxt("sales.tsv", delimiter='\t', dtype=float)
branches = data[:, 0] 
sales = data[:, 1:]          
sum_per_branch = np.sum(sales, axis=1)
order = np.argsort(sum_per_branch)[::-1]
print("Branch   Total Sales")
for i in order:
    print(f"{int(branches[i])}      {sum_per_branch[i]:.2f}")
