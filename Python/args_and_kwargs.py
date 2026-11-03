# # *args — Variable Positional Arguments
# def total(*args):
#     print(args) # args is a tuple
#     return sum(args)
# print(total(1, 2, 3)) # (1, 2, 3) then 6
# print(total(10, 20, 30, 40)) # (10,20,30,40) then 100
# print(total()) # () then 0


# # **kwargs — Variable Keyword Arguments
# def profile(**kwargs):
#     print(kwargs) # kwargs is a dict
#     for key, value in kwargs.items():
#         print(key, "=", value)
# profile(name="Amit", age=21, city="Varanasi")
# # {'name': 'Amit', 'age': 21, 'city': 'Varanasi'}
# # name = Amit / age = 21 / city = Varanasi



# def intro(**kwarg):
#     # print(kwarg)
#     for v in kwarg.values():
#         print(v)
        
#     # print(kwarg.keys())
    
# intro(name="Sachin",age=22,palce="Pune")



# # Combining All Argument Types
# def demo(a, b=10, *args, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("args:", args)
#     print("kwargs:", kwargs ) 
# demo(1, 2, 3, 4, x=5, y=6)
# # a: 1
# # b: 2
# # args: (3, 4)
# # kwargs: {'x': 5, 'y': 6}


# def add(*args,**kwargs):
#     print(sum(args))
#     print(sum(kwargs.values()))
    
# l1=[2,5,9,5]
# add(*l1)

# marks={
#     'a':20,
#     'b':25,
#     'c':50,
#     'd':5
# }

# add(**marks)



# def intro(**kwarg):
#     for v in kwarg.items():
#         print(v)
    
# intro(name="Sachin",age=22,palce="Pune")



# def multiply(*args):
#     mul=1
#     for i in args:
#         mul*=i
#     print(mul)
        
# multiply(2, 3, 4)


# def  how_many(*args):
#     print(len(args))
    
# how_many(2,5,5,8,9)


# def biggest(*args):
#     if len(args)==0:
#         print(None) 
#         return
#     maxium=0
#     for i in args:
#         if i>maxium:
#             maxium=i
#     print('Max :',maxium)
    
# biggest()

def f(a, b=2, *args, **kwargs):
 print(a, b, args, kwargs)
f(1)

    
