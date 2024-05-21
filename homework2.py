# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години,
# хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу
# // і % вам необхідно знайти відповідну кількість днів, годин, хвилин,
# а те що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)

# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

seconds_input = int(input("Введіть кількість секунд: "))

# Одна хвилина - 60 секунд
# Одна година - 3600 секунд
# Одна доба - 86400 секунд

# Визначаємо кількість днів
days = seconds_input // 86400
remaining_seconds = seconds_input % 86400

# Визначаємо кількість годин
hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600

# Визначаємо кількість хвилин
minutes = remaining_seconds // 60

# Визначаємо кількість секунд
seconds = remaining_seconds % 60

# Підбираємо правильну форму слова "день"
if days == 1:
    day_word = "день"
elif 2 <= days <= 4:
    day_word = "дні"
else:
    day_word = "днів"

# Форматуємо годинник, хвилини та секунди з провідними нулями
formatted_hours = str(hours).zfill(2)
formatted_minutes = str(minutes).zfill(2)
formatted_seconds = str(seconds).zfill(2)

# Формуємо результат
result = f"{days} {day_word}, {formatted_hours}:{formatted_minutes}:{formatted_seconds}"

# Виводимо результат
print(result)