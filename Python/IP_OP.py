# a = 10
# b = 3.14
# print(type(a)) # <class 'int'>
# print(type(b)) # <class 'float'>


# print(2 ** 1000)


# # / always returns float — even when it divides evenly!
# print(10 / 2) # 5.0 (not 5!)
# # // floors DOWN — watch with negatives!
# print(-7 // 2) # -4 (not -3!)
# # % gives remainder — useful for even/odd, last digit
# print(17 % 2) # 1 (odd)
# print(9876 % 10) # 6 (last digit!)


# # 135 minutes = ? hours and ? minutes
# hours, mins = divmod(220, 60)
# print(hours, mins) # 2, 15


# # What's the answer? Think before running!
# print(2 + 3 * 4 ** 2)


# name = input("Enter your name: ")
# print("Hello, " + name)
# print("Hello, ",name)

# _______________________________________________________________

# a = input("Enter first number: ") # user types 5
# b = input("Enter second number: ") # user types 3
# print(int(a) + int(b))
# a="24"
# b="54"
# a=int(a)
# b=int(b)
# print(a+b)


# # Trap 1: int() TRUNCATES — does NOT round!
# print(int(3.9)) # 3 (not 4!)
# print(int(-3.9)) # -3 (not -4!)
# # Trap 2: Can't convert invalid strings
# # int('hello') --> ValueError!
# # int('3.14') --> ValueError! (use float first)
# # Trap 3: bool() truthy/falsy values
# print(bool(0)) # False
# print(bool("")) # False (empty string)
# print(bool("hi")) # True
# print(bool(42)) # True



# # --- Simple Calculator ---
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print("Addition: ", num1 + num2)
# print("Subtraction: ", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division: ", num1 / num2)
# print("Floor Division:", num1 // num2)
# print("Modulus: ", num1 % num2)
# print("Power: ", num1 ** num2)


# r = float(input("Enter a radius:"))
# area_of_circle = 3.14159 * r ** 2
# print(f"Area of circle is {area_of_circle}")


# C = float(input("Enter a temperature:"))
# F = C * 9/5 + 32
# print(f"Celsius is {C} , convert to Fahrenheit is {F}")


# Take total seconds from user
total_seconds = int(input("Enter total seconds: "))

# Convert using // (integer division) and % (remainder)
hours   = total_seconds // 3600          # 1 hour = 3600 seconds
minutes = (total_seconds % 3600) // 60   # remaining seconds → minutes
seconds = total_seconds % 60             # remaining seconds

# Display result
print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")



# import math
# print(math.floor(-3.2)) # -4 (floors DOWN)
# print(math.floor(-3.5)) # -4 (floors DOWN)
# print(int(-3.5)) # -3 (truncates toward 0)


# print(0.1 + 0.2)