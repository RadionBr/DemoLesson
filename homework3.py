# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел,
# знаходить серед них унікальне число та повертати його. Унікальне число - це число,
# яке зустрічається в списку один раз. Випадок, коли в одному списку буде
# кілька унікальних чисел, перевіряти не потрібно.
#
# Приклад:
#
# def find_unique_value(some_list):
#    pass
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

from collections import Counter

def find_unique_value(some_list):
    # Використовуємо Counter для підрахунку кількості появ кожного елемента в списку
    count = Counter(some_list)
    # Проходимо по підрахунках і знаходимо елемент, який зустрічається один раз
    for num, freq in count.items():
        if freq == 1:
            return num
    # Якщо унікального числа не знайдено, повертаємо None (це необов'язково, залежить від вимог)
    return None

# Тестування функції
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")