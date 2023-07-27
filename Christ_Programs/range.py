import numpy as np

# Create a range of numbers from 0 to 9 (excluding 10)
arr = np.arange(10)
print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]

# Create a range of numbers from 5 to 15 (excluding 15) with a step of 2
arr = np.arange(5, 15, 2)
print(arr)  # Output: [ 5  7  9 11 13]


# access the index #1
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

indices = np.where(arr == 30)
print(indices)  # Output: (array([2]),)


#access the index #2

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

for index, value in np.ndenumerate(arr):
    print(index, value)

#o/p
# (0,) 10
# (1,) 20
# (2,) 30
# (3,) 40
# (4,) 50



