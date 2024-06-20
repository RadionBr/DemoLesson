# import random
# from random import randint, choice
# print(random.randint(1,100))
# print(random.random())
# print(random.choice("qwerty"))
# nums = [1, 2, 3, 4]
# random.shuffle(nums)


# import math
# print(-math.inf)
# print(math.sqrt())
# print(math.factorial(5))

# from decimal import *
# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.1")
# number = number + number + number
# print(number)

# import datetime as dt
#
# print(dt.date.today())
# print(dt.date(2022,11,10))
# print(dt.time)
# print(dt.datetime.now())

# class NotPozNum(Exception):
#     def __init__(self, error_message, input_value):
#         self.error_message = error_message
#         self.input_value = input_value
#
# try:
#     number = int(input("Pozitive: "))
#     if number < 0:
#         raise NotPozNum("provid", number)
# except NotPozNum as error:
#     print(error.args[0])
#     print(error.args[1])
# except Exception as error:
#     print(error)
