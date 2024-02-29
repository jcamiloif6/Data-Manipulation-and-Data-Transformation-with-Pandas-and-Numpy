import numpy as np

#arr1 = np.array([1,2,3])
#arr2 = np.array([4,5,6])

#arr = np.concatenate((arr1, arr2))

#arr3 = np.array([[1,2] , [3,4]])
#arr4 = np.array([[5,6] , [7,8]])

#print(arr4.shape)

#arr = np.concatenate((arr3, arr4), axis=1)

#print(arr)

#arr = np.array([1,2,3,4,5,6])

#newarr = np.array_split(arr, 3)

#print(newarr)

#arr = np.array([1,2,3,4,5,4,4])

#x =np.where(arr == 4)

#print(x)

"""
arr = np.array([3,2,0,1])

print(np.sort(arr))

a = np.array([[1,4],[3,1]])

print(np.sort(a))                # sort along the last axis


print(np.sort(a, axis=None))     # sort the flattened array


print(np.sort(a, axis=0))        # sort along the first axis

"""


dtype = [('name', 'S10'), ('height', float), ('age', int)]

values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),

          ('Galahad', 1.7, 38)]

a = np.array(values, dtype=dtype)       # create a structured array

print(np.sort(a, order='height'))