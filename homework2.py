# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
#
# При розв'язанні задачі зверніть увагу на наступні моменти:
#
# У рядку можуть зустрічаються крапки та/або коми
# Рядок може починатися з літери або, наприклад, з пробілу або точки
# У слові може бути апостроф і він є частиною слова
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
#
# Вихідні параметри: Рядок.

# def first_word(text):
#     """ Пошук першого слова """
#     pass
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

def first_word(text):
    """Знаходить перше слово в рядку."""
    # Замінюємо крапки та коми на пробіли
    text = text.replace('.', ' ').replace(',', ' ')
    # Розділяємо рядок на слова
    words = text.split()
    # Повертаємо перше слово
    return words[0]

# Тести
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
