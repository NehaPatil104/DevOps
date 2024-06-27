# # # # from random import random 
# # # # import math

# # # # print(math.floor(random() * (20- 15)) + 15)

# # # names = ((1, "a"), (2, "b"), (3, "c"))
# # # print("Names ", names)

# # # # add index 0
# # # names = ((0, "z"),) + names
# # # print(names)

# # # # last index
# # # names = names + ((4, "d"),)
# # # print(names)

# # # # middle
# # # names = names[:1] + ((5, "o"),) + names[1:]
# # # print(names)

# # # #delete from 0
# # # names = names[1:]
# # # print(names)

# # # # last 
# # # names = names[:-1:]
# # # print(names)

# # # # middle
# # # names = names[:2] + names[3:]
# # # print(names)

# # products = [
# #     {
# #         "name" : "Pen",
# #         "price" : 10
# #     },
# #     {
# #         "name": "Book",
# #         "price": 70
# #     },
# #     {
# #         "name": "Eraser",
# #         "price": 5
# #     }
# # ]

# # print(products)
# # products[1]["color"] = "Red"
# # print(products)

# # keys_size = len(products[0])
 
# # if keys_size > 3:
# #     del products[0]["name"]

# # print(products)


# def add(num1, num2):
#     return num1 + num2

# def subtract(num1: int, num2:int) -> int:
#     return num1 - num2

# def multiply(num1: float, num2:float) -> float:
#     return num1 * num2

# print(add(2,3))
# print(subtract(5,3))
# print(multiply(2.1,3.7))

# multiply_fn = multiply
# print(multiply_fn(5, 6))

# divide = lambda num1, num2 : num1 / num2

# print(divide(1000, 20))

# from typing import TypeVar

# T = TypeVar('T')

# def find(arr : list[T], goal: T) -> T | None:
#     for i in arr:
#         if i == goal:
#             return True
#     return False

# print(find ([3, "5",1,2], 0))   
# answer = find ([3, "5",1,2], 0)

#Car , Home, Personl 8, 10, 12


# def calculate(p, n, r):
#     return (p*n*r)/100

# loan = "home"
# p = 2000
# n = 2

# if loan == "car":
#     print(calculate(p, n, 8))
# elif loan == "home":
#     print(calculate(p, n, 10))
# elif loan == "personal":
#     print(calculate(p, n, 12)) 

#rate = 5

def loan_factory(rate):
     
    def calulator(p, n):
        return p * n * rate / 100
    
    def updated_r(updated_rate):
        nonlocal rate
        rate = updated_rate
        
    return [calulator, updated_r]

car_emi_cal, updated_rate = loan_factory(8)

#print(car_emi_cal(100, 2)) 

updated_rate(5)
print(car_emi_cal(2000, 2))




