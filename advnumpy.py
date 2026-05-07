import numpy as np
a = np.array([1,2,3])
b = a[:2]
b[0] = 99
print(a)

c = a.copy()
c[0] = 42
print(c)

import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
print("original matrix:\n", matrix)
print("Transposed Matrix:\n", matrix.T)


scores = np.random.randint(0, 101, size=100)
print("average score:", np.mean(scores))
print("highest score:", np.max(scores))
print("lowest score:", np.min(scores))