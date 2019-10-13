import numpy as np
names = locals()
for i in range(3):
    names['gg' + str(i)] = np.array([[i, i + 1, i + 2], [i + 1, i + 2, i + 3]])
print(gg1)
print(gg1[1])
tuples = ()
for j in range(2):
    tuples = tuples + (((gg0[j],) + (gg1[j],)),)
print(tuples)
a = np.array([1, 2, 3])
print(a)
tuples2 = ((tuples) + (np.array([0.0]),))
print(tuples2)

