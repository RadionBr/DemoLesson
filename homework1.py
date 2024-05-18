# #Змінна не може:
#
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може складатися тільки з одного нижнього підкреслення "_".
#
# Список зареєстрованих слів можна взяти із keyword.kwlist.
#
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні
import string
import keyword

user_input = input("Введите логин: ")

# Перевірка на зареєстровані слова
if user_input in keyword.kwlist:
    is_valid = False
# Перевірка на єдиний підкреслення "_"
elif user_input == "_":
    is_valid = True
# Перевірка, що рядок не починається з цифри
elif user_input[0].isdigit():
    is_valid = False
# Перевірка на великі літери
elif any(char.isupper() for char in user_input):
    is_valid = False
# Перевірка на пробіли та знаки пунктуації (окрім "_")
elif any(char in string.punctuation and char != "_" for char in user_input):
    is_valid = False
# Якщо всі перевірки пройдено, ім'я є допустимим
else:
    is_valid = True

print(is_valid)
