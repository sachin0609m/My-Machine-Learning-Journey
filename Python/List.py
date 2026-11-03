# # Creating Lists
# # Empty list
# items = []
# print(items)
# # List of numbers
# marks = [85, 90, 72, 60]
# print(marks)
# # Mixed data types allowed
# mixed = [1, "Rajeev", 3.14, True]
# print(mixed)
# # Using the list() constructor
# letters = list("python") # ['p','y','t','h','o','n']
# print(letters)


# # Indexing
# fruits = ["apple", "banana", "cherry","mango"]
# # 0 1 2 3
# # -4 -3 -2 -1
# print(fruits[0]) # apple
# print(fruits[2]) # cherry
# print(fruits[-1]) # mango (last item)
# print(fruits[-2]) # cherry


# # Slicing
# nums = [10, 20, 30, 40, 50, 60]
# print(nums[1:4]) # [20, 30, 40]
# print(nums[:3]) # [10, 20, 30] from start
# print(nums[3:]) # [40, 50, 60] till end
# print(nums[::2]) # [10, 30, 50] every 2nd
# print(nums[::-1]) # [60,50,40,30,20,10] reversed!


# # Looping throug list 
# fruits = ["Apple", "Banana", "Cherry","Mango"]
# for i in range(len(fruits)):
#     print(fruits[i],end=" ")

# for fruit in fruits:
#     print(fruit)
    
    
# tasks = ["code", "test"]
# print(tasks)

# tasks.append("deploy") # ['code','test','deploy']
# print(tasks)

# tasks.insert(1, "review") # ['code','review','test','deploy']
# print(tasks)

# tasks.remove("test") # ['code','review','deploy']
# print(tasks)

# last = tasks.pop() # last = 'deploy'
# print(tasks)

# tasks[0] = "design" # ['design','review']    
# print(tasks)


# data = [101, "Varanasi", 25.3, 82.9]
# # id, city, lat, lon = data
# # print(id, city, lat, lon)
# print(data[-2:len(data)+1])



# n=50 
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print("FIZZBUZZ",end=" , ")
#     elif i%5==0:
#         print("FIZZ",end=" , ")
#     elif i%5==0:
#         print("BUZZ",end=" , ")
#     else:
#         print(i,end=" , ")

# marks = [85,90,72,60,95]
# Sum=0
# for i in marks:
#     Sum+=i
# print(f"Sum of list is {Sum}")
# l=len(marks)
# avg=Sum/l
# print(f"List of avegage is {avg}")


# lists = [23,67,12,89,45]
# largest=float("-inf")
# for i in lists:
#     if i>largest:
#         largest=i
# print(f"Largest elemint in list is {largest}")


# n = int (input("Enter a number"))
# count=0
# for i in range(1,n+i):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")


# items = [1,2,2,3,4,4,5,6,6,24,24,24]
# dup = []
# for i in items:
#     count=0
#     for j in items:
#         if i==j:
#             count+=1
#     if count>1 and i not in dup:
#         dup.append(i)
# print(dup)



# n = int (input("Enter a number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")




# items = [3, 1, 3, 2, 3, 1, 2, 3]

# best_num = items[0]     # number with highest count so far
# best_count = 0          # highest count so far

# for num in items:
#     # Count how many times `num` appears
#     count = 0
#     for x in items:
#         if x == num:
#             count += 1

#     # Best-so-far update
#     if count > best_count:
#         best_count = count
#         best_num = num

# print(f"Most frequent number: {best_num} (appears {best_count} times)")



# items = [1, 2, 2, 3, 4, 4, 4, 5]

# unique = []                     # new empty list

# for num in items:
#     if num not in unique:       # append only if not already present
#         unique.append(num)

# print("Original :", items)
# print("Unique   :", unique)


items = [1, 2, 2, 3, 4, 4, 4, 5]
t1=set(items)
print(t1)
l1=list(t1)
print(l1)

