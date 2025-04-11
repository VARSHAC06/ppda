import numpy as np
def process_array():
arr = np.random.randint(1, 21, size=(3, 3))
print ("Original Array:")
print (arr)
Mean_Val = np.mean(arr)
print ("Mean of the array: ", Mean_Value)
arr[arr < 10] = 0
print ("Array after replacing elements less than 10 with 0:")
print (arr)
process_array()
