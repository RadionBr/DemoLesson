# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба,
# мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters,
# з усім набором потрібних букв

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

user_input = input("Введіть дві літери через дефіс: ")

# Peremennimi rozdelyaem na 2 chasti
start_char, end_char = user_input.split('-')

# usaem string.ascii_letters
start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char)

result = string.ascii_letters[start_index:end_index + 1]

print(result)