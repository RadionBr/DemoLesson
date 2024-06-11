###### OOP CLASS AND OBJECTS ########

#### FILES #### TEXT FILES ##########

##### FILES AND AFTER OOP
# file - resurs chto zagr v oper pan
#r - read
#w - write
#a - apend file open for zapis
#b - binary. Use for work with binary files

#v1
# try:
#     my_file = open("hello.txt","w")
#     try:
#         my_file.write("hello ds  sd df f a fas f")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)

# v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("wwwwwww")

#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("rrrrrrr\n\ttttttt\n")


# with open("hello.txt", "r") as myfile:
#v1
    # result = myfile.read()
    # print(result)

# result = myfile.readline()
# print(result)
# result = myfile.readline(1)
# print(result)


# import pickle
#
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "1122233"],
#     ["Rohn", "1122444233"],
#     ["Kohn", "112233233"]
#
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users,file)
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)
#     for users in users_from_file:
#         print(f"Name: {users[0]} Phone: {user[1]}")


#####
#import shelve #polochka
#import scv
#FILENAME = "users.csv"

##### OOP ######

#smotrim na vse kak na obiekti
#opisanie obiekta

class Car:
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"My car in garage: {self.name}")


bmw = Car("bmw x5")
toyota = Car("toyota camry")
nissan = Car("nissan z350")
rolse = Car("Rolse Royse")

bmw.show_info()
toyota.show_info()
nissan.show_info()
rolse.show_info()



###
# r (Read). Файл відкривається для читання. Якщо файл не знайдено, то генерується виняток FileNotFoundError
#
# w (Write). Файл відкривається для запису. Якщо файл відсутній, він створюється. Якщо такий файл вже є,
# то він створюється заново, і відповідно старі дані в ньому стираються.
#
# a (Append). Файл відкривається для запису. Якщо файл відсутній, він створюється.
# Якщо подібний файл вже є, дані записуються в його кінець.
#
# b (Binary). Використовується для роботи з бінарними файлами. Застосовується разом з іншими режимами – w або r.

# # v1
# try:
#     my_file = open("hello.txt", "w")
#     try:
#         my_file.write("hello")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)
#
# # v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("wwwwww")
#
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("rrrrr\ntttttt\n")


# with open("hello.txt", "r") as myfile:
#     # v1
#     # result = myfile.read()
#     # print(result)
#     # v2
#     # result = myfile.readline()
#     # print(result)
#     # result = myfile.readline(1)
#     # print(result)
#     # v3
#     # result = myfile.readlines()
#     # print(result)
#     # v4
#     # for line in myfile:
#     #     print(line, end="")
#     # v5
#     line = myfile.readline()
#     while line:
#         print(line, end="")
#         line = myfile.readline()

####
# FILENAME = "notes.txt"
# NOTES_COUNT = 3
#
# notes = []
#
# for i in range(NOTES_COUNT):
#     notes.append(input(f"Enter note: {i + 1}: ").strip())
#
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
#
# with open(FILENAME, "r") as file:
#     print(file.read())

####
# import pickle
#
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)  # серіалізація
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)  # десеріалізація
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")


# import shelve
#
# FILENAME = "notes"
#
# with shelve.open(FILENAME) as users:
#     users["John"] = "123456789"
#     users["Peter"] = "987654321"
#     users["Vasya"] = "1568654156"
#
# with shelve.open(FILENAME) as users:
#     users["Petya"] = "12312341234123"
#     print(users["Petya"])
#     print(users["John"])
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#
#     print(users)
#     users.pop("John", "not found")
#
#     print("-" * 10)
#
#     for key in users:
#         print(f"{key} - {users[key]}")

####
import csv

FILENAME = "users.csv"


# v1
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Anton", "111111"]
#     writer = csv.writer(file)
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"{row[0]} - {row[1]}")

# v2
# users = [
#     {"name": "John", "phone": "111"},
#     {"name": "Petya", "phone": "222"},
#     {"name": "Vasya", "phone": "333"},
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "phone"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#
#     # all users
#     writer.writerows(users)
#
#     # one user
#     user: dict = {"name": "Test", "phone": "555"}
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['name'], " - ", row['phone'])

###
# import os

# os.mkdir("test_folder")

# os.rmdir("test_folder")

# file_name = "users.csv"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# доп: написати скрипт для видалення всіх файлів вказаної директорії
#
# # відносний шлях - щодо поточної директорії (папки, де знаходиться вихідник, який ви запустили)
# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("hello world")
# #
# with open("../../test1.txt", "w") as myfile:
#     myfile.write("hello world")
# абсолютний шлях - повний шлях починаючи з диска C://test_folder/...

##
# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени

#####
# class Car:
#     def __init__(self, name):
#         self.name = name
#
#     def show_info(self):
#         print(f"My car: {self.name}")
#
#
# bmw = Car("BMW X5")
# toyota = Car("TOYOTA Camry")
#
# bmw.show_info()
# toyota.show_info()

# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.

# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації

################################################################
# статичний метод (функція), поле (змінна) відносяться до класу, і до екземпляра
# статичний ел-т можна використовувати не створюючи екземпляр класу
# Найчастіше статичні класи використовують для опису конфігів та інших службових об'єктів, там де немає сенсу
# створювати екземпляри
# class Test:
#     # конструктор без параметрів (не за замовчуванням)
#     def __init__(self):
#         self.text = "some text"
#
#     # конструктор класу - створює екземпляр об'єкту
#     # def __new__(cls):
#     #     pass
#
#     # для ініціалізації об'єкту
#     # якщо явно не визначити конструктор __new__ -> то __init__ він створиться автоматично
#     # def __init__(self):
#     #     pass
#
#     @staticmethod
#     def show():
#         print("this is test class")
#         # print(self.text)
#
#     def demo_func(self):
#         print(f"this is demo func with value: {self.text}")
#
#
# my_test1 = Test()
# my_test1.show()
#
# my_test2 = Test()
# my_test2.show()
# my_test2.demo_func()
#
# Test.show()
# Test.demo_func(my_test2)

##
# class Person:
#     # __init__ Конструктор класу – дозволяє створити екземпляр класу. Можливо з параметрами та без параметрів.
#     # self - посилання на контекст класу, екземпляр класу
#     # контекст класу - все що є частиною класу (экземпляра) -
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_person(self):
#         print(f"Name: {self.name} age: {self.age}")
#
#
# user1 = Person("Vasya", 33)
# user2 = Person("Petya", 44)
# user1.show_person()
# user2.show_person()
# print(user1.name)

# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self): # lemon, price: 5
#         # print(self.dimensions)
#         return f"{self.name}, price: {self.price}"
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name.title()} {self.surname.title()}"
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         all_products = ""
#         for product, count in self.products.items():
#             all_products += f"\n{product.name}: {count} pcs."
#         return f"User: {self.user}\nItems:{all_products}"
#
#     # """
#     # User: Ivan Ivanov
#     # Items:
#     # lemon: 4 pcs.
#     # apple: 20 pcs.
#     # """
#
#     def get_total(self):
#         all_sum = 0
#         for product, count in self.products.items():
#             all_sum += (product.price * count)
#         return all_sum
#
#
# lemon = Item('lemon', 5, "yellow", "small")
# print(lemon)
# # test1 = lemon.__str__()
# # print(test1)
# # test2 = str(lemon)
# # print(test2)
# apple = Item('apple', 2, "red", "middle")
# # print(lemon)  # lemon, price: 5
# buyer = User("Ivan", "Ivanov", "02628162")
# print(buyer)  # Ivan Ivanov
# #
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# print(cart.get_total())
# # """
# # User: Ivan Ivanov
# # Items:
# # lemon: 4 pcs.
# # apple: 20 pcs.
# # """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# # """
# # User: Ivan Ivanov
# # Items:
# # lemon: 4 pcs.
# # apple: 10 pcs.
# # """
# #
# assert cart.get_total() == 40

####
# import re
#
# with open("draft.html", "r", encoding="utf-8") as html_file:
#     for line in html_file:
#         text = re.findall(r">[a-zA-ZА-Яа-я]+", line)
#         if len(text) > 0:
#             print(text)

############
# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
#
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
#
# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
#
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
#
# За підсумками роботи програми необхідно показати статистику дій.
#
# Наприклад, якщо й у нас є такий текст:
#
# To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep
#
# Неприпустиме слово: die.
#
# Результат:
#
# To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To ***: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To ***, to sleep.
#
# Статистика: 2 заміни слова die.
#
# Нотатка:
#
# Текст для всіх завдань можна написати самостійно або взяти з Інтернету.
#
# Логіка має працювати з будь-яким текстом.






























