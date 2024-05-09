"""ROZDEL 1 ELEMENT NA 2 SPISKA
Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
Тобто, в результаті повинен вийти список із 2-х списків.
Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
Важливо! Потрібно створити рішення,
яке обробляє 3 випадки - список порожній, у списку парна кількість елементів і в списку непарна кількість елементів.
Приклади:
Було => стало
"""


#nayti indeks seredini
#ponyat kolichestvo i podelit potom na celo
#slices //

spisok = [1, 2, 3, 4, 5, 6]

# Proveryaem na pustotu spiska
if len(spisok) == 0:
    result = [[], []]  # sozdaem 2 pustih spiska po rezultatu
# Razdelim ego na 2 chasti takim obrazom len dlina spiska
elif len(spisok) % 2 == 0:
    middle = len(spisok) // 2  # delim na polovinu dlya ponyatiya sredini spiska
    result = [spisok[:middle], spisok[middle:]]  # rozdelyaem takim obrazom na 2 parts

print(result)