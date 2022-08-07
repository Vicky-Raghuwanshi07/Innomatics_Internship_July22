import numpy as np

np.set_printoptions(legacy='1.13')
a = list(map(float, input().split()))
a = np.array(a)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))


