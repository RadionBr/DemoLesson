"""Програма має виконувати прості математичні дії (+, -, *, /).
Користувачеві пропонується почерзі ввести числа та дію над цими числами,
 програма, виходячи з дії, обчислює та друкує результат.
Зробити перевірку на те, що при діленні дільник не дорівнює 0!"""

#tut nado isspolzovat if i elif
#usanul case (on dobrotniy)
#ostalnoe po lekcii chto bilo

chislo = int(input("1. splusovat\n2. otnimanie\n3. umnojenie\n4. delenie\nSelect your choice: "))

num1 = int(input("Vvedite chislo 1: "))
num2 = int(input("Vvedite chislo 2: "))

match chislo:
    case 1:
        result = num1 + num2
        print("splusovivaem...", result)
    case 2:
        result = num1 - num2
        print("otnimaem", result)
    case 3:
        result = num1 * num2
        print("umnojaem", result)
    case 4:
        if num2 == 0:
            print("oshibka delenia na zero!")
        else:
            result = num1 / num2
            print("delim", result)
    case _:
        print("ne verniy vvod")