# # Lambda — the One-Line Function
# # a normal function
# def square(x):
#  return x ** 2
# # the same thing as a lambda
# square = lambda x: x ** 2
# print(square(5)) # 25
# # multiple arguments
# add = lambda a, b: a + b
# print(add(3, 4)) # 7

# Sum = lambda *args : sum(args)
# print(Sum(2,5,48))


# # custom sorting
# students = [("Amit", 85, .254), ("Neha", 92, .444), ("Ravi", 78, .944)]
# students.sort()
# print(students)
# students.sort(key=lambda s: s[2])
# students.sort(key=lambda s: s[1])
# students.sort(key=lambda s: s[0]) 

# print(students) # [('Neha',92),('Amit',85),('Ravi',78)]



# # map()
# nums = [2,6,4,2,8,9]
# sqr=list(map(lambda n:n**2 , nums))
# print(sqr)

# # convert strings to integers
# strs = ["10", "20", "30"]
# ints = list(map(int, strs))
# print(ints) # [10, 20, 30]



# # filter()
# nums = [1, 2, 3, 4, 5, 6]
# evens = list(map(lambda x : x**3 ,filter(lambda x: x % 2 == 0 , nums)))
# print(evens) # [2, 4, 6]

# words = ["hi", "python", "ok", "lambda"]
# long = list(filter(lambda w: len(w) > 2, words))
# print(long) # ['python', 'lambda']



# # reduce()
# from functools import reduce
# nums = [1, 2, 3, 4]
# product = reduce(lambda a, b: a * b, nums)
# print(product) # 24 (1*2*3*4)


# total = reduce(lambda a, b: a + b, nums)
# print(total) # 10



# raw = ["₹100", "₹250", "₹80"]
# prices = list(map(lambda p: int(p.replace("₹", "")), raw))
# print(prices) # [100, 250, 80]
# # keep only passing scores
# scores = [45, 82, 33, 91, 67]
# passed = list(filter(lambda s: s >= 40, scores))
# print(passed) # [45, 82, 91, 67]
# # total revenue with reduce
# from functools import reduce
# revenue = reduce(lambda a, b: a + b, prices)
# print(revenue) # 430




# '''
# Double Every Number
# Given nums = [1, 2, 3, 4, 5] , use map() with a lambda to build a list where
# every number is doubled.
# Uses: map + lambda
# '''
# nums = [1, 2, 3, 4, 5]

# double = list(map(lambda x : x*2 , nums))

# print(f"Every number are doubled :{double}")



# '''
# Keep the Positives
# Given nums = [-3, 5, -1, 8, 0, -7, 2] , use filter() with a lambda to keep
# only the positive numbers.
# Uses: filter + lambda
# '''
# nums = [-3, 5, -1, 8, 0, -7, 2]

# positive = list(filter(lambda x : x>=0 , nums))

# print(f"Positive Number :{positive}")



# '''
# Cube with Lambda
# Write a lambda cube that returns the cube of a number. Test it on 2, 3, and 5.
# Hint: cube = lambda x: x ** 3
# '''
# a=int(input("Enater a number :"))
# cube = lambda x : x**3
# print(cube(a))



# '''
# Uppercase All
# Given words = ["python", "lambda", "map"] , use map() to build a list of the
# words in UPPERCASE.
# Hint: map(lambda w: w.upper(), words)
# '''
# words = ["python", "lambda", "map"]
# UpperCase = list(map(lambda w:w.upper(),words))
# print(UpperCase)



# '''
# Filter the Odds
# Given numbers 1 to 20, use filter() to keep only the odd numbers.
# Hint: filter(lambda x: x % 2 != 0, range(1, 21))
# '''
# odds = list(filter(lambda x :x%2!=0 , range(1,21)))
# print(odds)



# '''
# Sum with reduce
# Using reduce() , find the sum of all numbers in [5, 10, 15, 20] . Then modify it
# to find the maximum instead.
# '''
# from functools import reduce
# nums = [5, 10, 15, 20]

# Sum = reduce(lambda a,b:a+b , nums)
# print(f"Sum of all numbers is {Sum}")

# maximum = reduce(lambda a,b : a if a >b else b , nums )
# print(f"Maximum  instead is {maximum}")



# '''
# Sort by Last Letter
# Given names = ["Amit", "Neha", "Ravi", "Sara"] , sort them by their last letter
# using sorted() with a lambda key.
# Hint: sorted(names, key=lambda n: n[-1])
# '''
# names = ["Amit", "Neha", "Ravi", "Sara"]
# # names.sort(key=lambda n : n[0])
# # print(names)
# Sort = list(sorted(names, key=lambda n: n[-1]))
# print(Sort)



'''
Clean the Prices
Given raw = ["$100", "$250", "$99"] , use map() to strip the $ and convert
each to an integer. Then use filter() to keep only prices above 100.
Hint: chain map then filter; p.replace("$", "") .
'''
raw = ["$100", "$250", "$99", "$150"]
strip = list(map(lambda p : int(p.replace("$","")),raw))
prices = list(filter(lambda x: x>100,strip))
print(f"Prices :{strip}")
print(f"Prices above 100 is :{prices}")



from functools import reduce
words=["hi", "python", "lambda", "ok"]
max_word = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print (max_word)


nums = [1, 2, 3, 4, 5]
r = list(map(lambda x: x * 2, filter(lambda x: x > 2, nums)))
print(r)