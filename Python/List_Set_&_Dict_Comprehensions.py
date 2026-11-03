# # List Comprehension (Recap)
# # the old way
# squares = []
# for x in range(1, 6):
#  squares.append(x ** 2)
# # the comprehension
# squares = [x ** 2 for x in range(1, 6)]
# print(squares) # [1, 4, 9, 16, 25]

# # With a filter
# evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens) # [2, 4, 6, 8, 10]



# # Set Comprehension
# squares = {x * x for x in range(6)}
# print(squares) # {0, 1, 4, 9, 16, 25}

# # duplicates auto-removed
# lengths = {len(w) for w in ["hi", "ok", "python"]}
# print(lengths) # {2, 6} ("hi" and "ok" both give 2)



# # Dictionary Comprehension
# words = ["hi", "python", "set"]
# lengths = {w: len(w) for w in words}
# print(lengths) # {'hi': 2, 'python': 6, 'set': 3}

# squares = {n: n * n for n in range(1, 5)}
# print(squares) # {1: 1, 2: 4, 3: 9, 4: 16}
# print(squares[3]) # 9 (instant lookup)

# nums = [1, 2, 3, 4, 5, 6]
# even_sq = {n: n * n for n in nums if n % 2 == 0}
# print(even_sq) # {2: 4, 4: 16, 6: 36}



'''
Squares List
Use a list comprehension to build the squares of numbers 1 to 10. Then make a
second version that keeps only the even squares.
Hint: add if x % 2 == 0 for the filtered version.
'''
l1 = [i*i for i in range(1,11) if i%2==0]

print(l1) # [4, 16, 36, 64, 100]



'''
Cube Lookup Table
Use a dictionary comprehension to build {n: n*n*n} (cubes) for numbers 1 to 6.
Then look up and print the cube of 4.
Hint: build the dict, then access table[4] .
'''
num = [1,2,3,4,5,6]

cube = {n: n*n*n for n in num}

print(cube) #{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}



'''
Vowel Set
Take a word from the user. Use a set comprehension to collect all the unique
vowels that appear in it. Example: "varanasi" → {'a', 'i'} .
Hint: {ch for ch in word if ch in "aeiou"}
'''
word = input("Enter any word: ")

vowels = {ch for ch in word.lower() if ch in "aeiou"}

print(vowels)



'''
Price with Tax
Given prices = {"pen": 10, "book": 50, "bag": 200} , use a dictionary
comprehension to build a new dict where every price is increased by 18% tax.
Hint: {item: price * 1.18 for item, price in prices.items()}
'''
prices = {"pen": 10, "book": 50, "bag": 200} 

tex = {item: price * 1.18 for item, price in prices.items()}

print(tex)



'''
Word Frequency
Take a sentence from the user. Using a dictionary comprehension over the unique
words, build {word: count} showing how many times each word appears.
Example: "a b a c b a" → {'a': 3, 'b': 2, 'c': 1} .
Hint: split into words, then {w: words.count(w) for w in set(words)} .
'''
sentence = input("Enter a sentence: ")

words = sentence.split()                      # list of words
unique_words = set(words)                     # unique words only

# Dictionary comprehension: {word: count}
freq = {w: words.count(w) for w in unique_words}

print(freq)

