import numpy as np
import sys

l = range(1000)
print(" --> ", sys.getsizeof(1) * len(l))

l1 = np.arange(1000)
print(l1.size * l1.itemsize)
