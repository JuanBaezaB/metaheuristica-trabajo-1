import numpy as np

my_array = np.arange(12).reshape(3, 4)
print("Original array:")
print(my_array)

rows, columns= my_array.shape
print('row:', rows, ' columns:', columns)
#columns -=1
print('row:', rows, ' columns:', columns)
for i in range(20):
    print(np.random.randint(0, columns))