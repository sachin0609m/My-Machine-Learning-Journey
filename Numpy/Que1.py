import numpy as np

# # 1. Create an array of 20 random exam marks between 0 and 100 with np.random.randint , then print mean, max, min and standard deviation.
# arr = np.random.randint(0, 101, size=20)
# print(f"Exam marks: {arr}")
# print(f"Mean: {np.mean(arr)}")
# print(f"Max: {np.max(arr)}")
# print(f"Min: {np.min(arr)}")
# print(f"Standard Deviation: {np.std(arr)}")


# # 2. Use a boolean mask to print only the marks above the mean, and count them.
# arr = np.random.randint(0, 101, size=20)
# mean = np.mean(arr)
# above_mean = arr[arr > mean]
# print(f"Marks above mean: {above_mean}")
# print(f"Count of marks above mean: {len(above_mean)}")


# # 3. Build np.arange(20).reshape(4, 5) . Print its second column, its last row, and its column means.
# arr2d = np.arange(20).reshape(4, 5)
# print(f"2D array:\n{arr2d}")
# print(f"Second column: {arr2d[:, 1]}")
# print(f"Last row: {arr2d[-1, :]}")
# print(f"Column means: {np.mean(arr2d, axis=0)}")
# print(f"Row means: {np.mean(arr2d, axis=1)}")


# 4. Subtract the column means from every row in one line, and explain in a sentence why that works.
arr2d = np.arange(20).reshape(4, 5)
arr2d_centered = arr2d - np.mean(arr2d, axis=0)
print(f"Array after subtracting column means:\n{arr2d_centered}")




