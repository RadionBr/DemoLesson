# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range)
# для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
#
# def common_elements():
# 		pass
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


def common_elements():
    # Генеруємо два списки з чисел кратних 3 і 5
    multiples_of_3 = {i for i in range(100) if i % 3 == 0}
    multiples_of_5 = {i for i in range(100) if i % 5 == 0}

    # Знаходимо перетин двох множин
    common_multiples = multiples_of_3 & multiples_of_5

    return common_multiples


# Перевірка функції за допомогою assert
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

# Виклик функції для перевірки результату
print(common_elements())