# i=4
# while i<=5:
#     print("Hello")
#     i+=1
# else:
#     print("End")


# for i in range (1,10):
#     print(i,end=" ")
# print()  
    
# for i in range (1,10):
#     if i==5:
#         break
#     print(i,end=" ")
# print()  
        

# for i in range (1,10):
#     if i==5:
#         continue
#     print(i,end=" ")
        
# n=5
# for i in range (1,11):
#     print(n*i)


# for i in range(1, 21):
#     if i % 2 != 0:      # if number is odd
#         continue        # skip the rest, go to next iteration
#     print(i, end=" ")
# print()

# n=100
# sum=n*(n+1)/2
# print(sum)


# # Write a multiplication table, factorial, and sum from 1 to N.
# # Table
# n=int(input(f"Enter a table number:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")
    
# # Factorial
# n=int(input(f"Enter a number:"))
# fac=1
# for i in range (1,n+1):
#     fac*=i
# print(fac)

# # Sum
# n=int(input(f"Enter a number:"))
# sum=0
# for i in range (1,n+1):
#     sum+=i
# print(sum)
# # sum=n*(n+1)/2
# # print(sum)

# n=int(input(f"Enter a number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# n = int(input("Enter a number: "))
# i = 1
# print(f"Factors of {n}: ",end=" ")

# while i <= n:
#     if n % i == 0:          # i divides n exactly
#         print(i, end=" ")
#     i += 1                  # IMPORTANT: update i, else infinite loop
    
    
    
    
# n = int(input("Enter a number: "))

# i = 1
# while i <= 10:
#     print(f"{n}x{i}={n*i}")
#     i += 1


# for i in range(1,6):
#     for j in range(1,6):
#         if j<=6-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



for i in range(1,4):
    for j in range(1,6):
        if j>=i and j<=6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()







                 