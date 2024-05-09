# n1 = 10
# n2 = 20
#
# n1, n2 = 10, 20 #mnoj prisvoenie
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 != n2)
#
# print(1 == 1 and 3 == 3)
# print(1 == 1 and 2 == 3)

# is_valid = False
# print(is_valid)
# print(not is_valid) # not inversia, esli False stanet true

# print("hello" in "hello world")

#v1
# hours = int(input("Enter ours: "))
# if hours >= 12:
#     print("PM")
# else:
#     print("AM")

# v2

# if 12 <= hours < 24:
#     print("PM")
# elif 0 <= hours < 12:
#     print("AM")
# else:
#     print("Incor")

# reyt filma = 5 or 4 - ok else ploho


# film_raiting = int(input("Enter film rait: "))
# if film_raiting > 0 and film_raiting <= 5:
#     if film_raiting == 4 or film_raiting == 5:
#         print("Film ok!")
#     else:
#         print("Film not ok")
# else:
#     print("incorrect rait !")

###
# vvesti s kalvi 3 chisla
# naymensh s 3h chisel
# kilkist odn chisel

# number1 = int(input("Enter fist number: "))
# number2 = int(input("Enter sec number: "))
# number3 = int(input("Enter third number: "))
#
# if number1 <= number2 <= number3:
#     if number1 < number3:
#         print(number1)
#     else:
#         print(number3)
# elif number2 <= number3:
#     if number2 < number1:
#         print(number2)
#     else:
#         print(number1)
# elif number3 <= number1:
#     if number3 < number1:
#         print(number1)
#     else:
#         print(number3)
# else:
#     print("All numbers are equal")


# Kilkist odnakovih chisel

# if number1 == number2 == number3:
#     print(3)
# elif number1 == number2 or number1 == number3 or number2 == number3:
#     print(2)
# else:
#     print(0)

# user_select = int(input("1. Start\n2. Settings\n3. Saved games\n4. Exit\nSelect your choice: "))
#
# if user_select == 1:
#     print("start game...")
# elif user_select == 2:
#     print("Settings")
# elif user_select == 3:
#     print("Saved games")
# elif user_select == 4:
#     print("exit")
# else:
#     print("Invaild input. type again")
#
# #v2
#
# match user_select:
#     case 1:
#         print("Start game...")
#     case 2:
#          print("Settings")
#     case 3:
#          print("saved games")
#     case 4:
#          print("exit")
#     case _:
#         print("Invaold")

######################################################## SPISKI
# lisst
# numbers = []
# numbers_1 = list()
# print(type(numbers))
# print(type(numbers_1))

numbers = [1, 3, 25, 7, 2, 7]

print(numbers)
print(numbers[0])


# zamena znachenia po poryadkovomu nomeru
numbers[1] = 111111
print(numbers)
print(len(numbers))
# -1 poslednie chislo
print(numbers[-1])

print(numbers[len(numbers) -1]) #numbers 6
