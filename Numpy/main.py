import numpy as np
import time

arr = np.arange(1000000)
lis = list(range(1000000))
start_time = time.time()
print(f"Sum of array = {arr.sum()}")
print(f"Time taken to sum the array: {time.time() - start_time}")
print(f"Sum of list = {sum(lis)}")
print(f"Time taken to sum the list: {time.time() - start_time}")
#----------------------------------------------------------------------------
# Creating arrays
a = np.array([1,2,3,4,5])
print(f"a = {a}")
print(f"a[0] = {a[0]}")  # Output: 1
print(f"a[-1] = {a[-1]}")  # Output: 5

b = np.zeros(3)
print(f"zeros 1D array = {b}")
b1 = np.zeros((3, 4))
print(f"zeros 2D array = {b1}")

c = np.ones(3)
print(f"ones 1D array = {c}")    
c1 = np.ones((3, 4))
print(f"ones 2D array = {c1}")

d = np.arange(10)
print(f"arange = {d}")
d1 = np.arange(1, 10, 2)
print(f"arange with step = {d1}")

e = np.linspace(0, 1, 5)
print(f"linspace = {e}")

#---------------------------------------------------------------

# 2D Arrau 
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array \n{arr2d}")
print(f"Shape of 2D array = {arr2d.shape}")
print(f"Number of dimensions = {arr2d.ndim}")
print(f"Size of 2D array = {arr2d.size}")
print(f"Data type of 2D array = {arr2d.dtype}")

#---------------------------------------------------------------

a1 = np.arange(5 , 51 , 5)
print(f"arange = {a1}")
print(f"Shape of 1D array = {a1.shape}")
print(f"Number of dimensions = {a1.ndim}")

reshaped_arr = a1.reshape(2, 5)
print(f"Reshaped array = \n{reshaped_arr}")

#---------------------------------------------------------------

# Indexing and slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Output: 10

print(arr[1:4])  # Output: [20 30 40]

print(arr[-1])  # Output: 50

#---------------------------------------------------------------

# Indexing and slicing 2D arrays
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])

print(arr2d[0, 1])  # Output: 2

print(arr2d[1, 2])  # Output: 6

print(arr2d[2, 0])  # Output: 7

print(arr2d[:, 1])  # Output: [2 5 8]

print(arr2d[0:2, 1:3])  # Output: [[2 3]
                        #          [5 6]]

#---------------------------------------------------------------

score  = np.array([85, 90, 78, 45, 92, 88, 76, 95, 89, 84])

mean_score = np.mean(score)
print(mean_score)

marks_above = score > 80
print(marks_above) 

print(score[marks_above])  # Output: [85 90 92 88 95 89 84]
print(score[marks_above].mean())  # Output: 89.28571428571429

#---------------------------------------------------------------

marks = np.array([45, 82, 67, 91, 38, 74, 59, 88])

marks1= marks[marks >= 60]
count= len(marks1)
print(count)

average= np.mean(marks)
print(average)

marks= marks[(marks >= 60) & (marks < 85)]
print(marks)

