import numpy as np
p1 = np.array(input("Input coordinate of P1: ").split(), dtype=float)
p2 = np.array(input("Input coordinate of P2: ").split(), dtype=float)
p3 = np.array(input("Input coordinate of P3: ").split(), dtype=float)
def dist(a, b):
    return np.sqrt(np.sum((a - b)**2))
d12 = dist(p1, p2)
d23 = dist(p2, p3)
d31 = dist(p3, p1)
longest = max(d12, d23, d31)

print(f"Output:\nThe longest distance = {longest:.2f}")
