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
