import numpy as np
import pandas as pd
a = pd.DataFrame({0: [1, 2, 3], 1: [4, 5, 6]})
print(a.index[1])
b = a.rename(index={0: 1, 1: 1, 2: 1})
print(b.index[1])
ix = np.array(a.index[0])
print(ix)
