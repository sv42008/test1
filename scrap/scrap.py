import numpy as np

a = np.arange(24).reshape(4, 6)
print(a[[1], :])

print(a)
print(a[1: 4, :])

print(round(5.2/2, 0))