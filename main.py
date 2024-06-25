from accessify import private, protected, implements


class ICar:
    def show(self):
        pass

    def test(self):
        pass


@implements(ICar)
class Car:
    @private  # доступ будет только внутри этого класса
    def show_secret(self):
        print("Secret token")

    @protected  # доступ будет внутри этого класса и в дочерних
    def show_data_for_child_classes(self):
        print("Data for child classes")

    # доступ будет везде
    def show(self):
        print("Info from secret method")
        self.show_secret()
        print("Info from protected method")
        self.show_data_for_child_classes()

    def test(self):
        print("Test method")


class SuperCar(Car):
    def show_parent_methods(self):
        # print("Info from secret method")
        # self.show_secret()
        print("Info from protected method")
        self.show_data_for_child_classes()


super_car = SuperCar()
super_car.show_parent_methods()
# super_car.show_data_for_child_classes()

# car1 = Car()
# car1.show()
# car1.test()
# car1.show_data_for_child_classes()
# car1.show_secret()

# Mixin классы - это классы у которых нет данных, но есть методы.
# Mixin используются для добавления одних и тех же методов в разные классы.
#
# В Python примеси делаются с помощью классов.
# Так как в Python нет отдельного типа для примесей, классам-примесям принято давать имена заканчивающиеся на Mixin.
#
# С одной стороны, то же самое можно сделать с помощью наследования обычных классов, но не всегда те методы,
# которые нужны в разных дочерних классах, имеют смысл в родительском.

# class Radio:
#     def play_song(self):
#         pass
#
#     def set_station(self, station):
#         pass
#
#
# class RadioUserMixin(object):
#     def __init__(self):
#         self.radio = Radio()
#
#     def play_song_on_station(self, station):
#         self.radio.set_station(station)
#         self.radio.play_song()
#
#
# class Vehicle:
#     pass
#
#
# class Car(Vehicle, RadioUserMixin):
#     pass

# class Rational:
#     def __init__(self, a=0, b=1):
#         a = int(a)
#         b = int(b)
#         if b == 0:
#             raise ValueError("Illegal value of the denominator")
#         self.__numerator = a
#         self.__denominator = b
#         self.__reduce()
#
#     # Сокращение дроби.
#     def __reduce(self):
#         # Функция для нахождения наибольшего общего делителя
#         def gcd(a, b):
#             if a == 0:
#                 return b
#             elif b == 0:
#                 return a
#             elif a >= b:
#                 return gcd(a % b, b)
#             else:
#                 return gcd(a, b % a)
#         sign = 1
#         if (self.__numerator > 0 > self.__denominator) or \
#                 (self.__numerator < 0 < self.__denominator):
#             sign = -1
#         a, b = abs(self.__numerator), abs(self.__denominator)  # abs -> вернет положительное число
#         c = gcd(a, b)
#         self.__numerator = sign * (a // c)
#         self.__denominator = b // c
#
#         # Клонировать дробь.
#     def __clone(self):
#         return Rational(self.__numerator, self.__denominator)
#
#     @property
#     def numerator(self):
#         return self.__numerator
#
#     @numerator.setter
#     def numerator(self, value):
#         self.__numerator = int(value)
#         self.__reduce()
#
#     @property
#     def denominator(self):
#         return self.__denominator
#
#     @denominator.setter
#     def denominator(self, value):
#         value = int(value)
#         if value == 0:
#             raise ValueError("Illegal value of the denominator")
#         self.__denominator = value
#         self.__reduce()
#
#     # Привести дробь к строке.
#     def __str__(self):
#         return f"{self.__numerator} / {self.__denominator}"
#
#     def __repr__(self):
#         return self.__str__()
#
#     # Привести дробь к вещественному значению.
#     def __float__(self):
#         if self.__denominator == 0:
#             raise ZeroDivisionError()
#         return self.__numerator / self.__denominator
#
#     # Привести дробь к логическому значению.
#     def __bool__(self):
#         return self.__numerator != 0
#
#     # Сложение обыкновенных дробей.
#     def __iadd__(self, rhs):  # +=
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.denominator + \
#                 self.denominator * rhs.numerator
#             b = self.denominator * rhs.denominator
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     # drob1 + drob2 ====> drob1 += drob2
#     def __add__(self, rhs):  # +
#         return self.__clone().__iadd__(rhs)
#
#     # Вычитание обыкновенных дробей.
#     def __isub__(self, rhs):  # -=
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.denominator - \
#                 self.denominator * rhs.numerator
#             b = self.denominator * rhs.denominator
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     def __sub__(self, rhs):  # -
#         return self.__clone().__isub__(rhs)
#
#     # Умножение обыкновенных дробей.
#     def __imul__(self, rhs):  # *=
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.numerator
#             b = self.denominator * rhs.denominator
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     def __mul__(self, rhs):  # *
#         return self.__clone().__imul__(rhs)
#
#     # Деление обыкновенных дробей.
#     def __itruediv__(self, rhs):  # /=
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.denominator
#             b = self.denominator * rhs.numerator
#             if b == 0:
#                 raise ValueError("Illegal value of the denominator")
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     def __truediv__(self, rhs):  # /
#         return self.__clone().__itruediv__(rhs)
#
#     # Отношение обыкновенных дробей.
#     def __eq__(self, rhs):  # ==
#         if isinstance(rhs, Rational):
#             return (self.numerator == rhs.numerator) and \
#                    (self.denominator == rhs.denominator)
#         else:
#             return False
#
#     def __ne__(self, rhs):  # !=
#         if isinstance(rhs, Rational):
#             return not self.__eq__(rhs)
#         else:
#             return False
#
#     def __gt__(self, rhs):  # >
#         if isinstance(rhs, Rational):
#             return self.__float__() > rhs.__float__()
#         else:
#             return False
#
#     def __lt__(self, rhs):  # <
#         if isinstance(rhs, Rational):
#             return self.__float__() < rhs.__float__()
#         else:
#             return False
#
#     def __ge__(self, rhs):  # >=
#         if isinstance(rhs, Rational):
#             return not self.__lt__(rhs)
#         else:
#             return False
#
#     def __le__(self, rhs):  # <=
#         if isinstance(rhs, Rational):
#             return not self.__gt__(rhs)
#         else:
#             return False
#
#
# if __name__ == '__main__':
#     r1 = Rational(3, 4)
#     print(float(r1))
#     print(r1)
#     print(f"r1 = {r1}")
#     r2 = Rational(5, 6)
#     # r1 += r2
#     print(r1)
#     print(f"r2 = {r2}")
#     print(f"{r1} + {r2} = {r1 + r2}")
#     print(f"{r1} - {r2} = {r1 - r2}")
#     print(f"{r1} * {r2} = {r1 * r2}")
#     print(f"{r1} / {r2} = {r1 / r2}")
#     print(f"{r1} == {r2} {r1 == r2}")
#     print(f"{r1} != {r2} {r1 != r2}")
#     print(f"{r1} > {r2} {r1 > r2}")
#     print(f"{r1} < {r2} {r1 < r2}")
#     print(f"{r1} >= {r2} {r1 >= r2}")
#     print(f"{r1} <= {r2} {r1 <= r2}")


####
# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Price: {self.price}")
#
#     def __add__(self, other):
#         if isinstance(other, Car):
#             return self.price + other.price
#         elif other > 0:
#             return self.price + other
#         else:
#             raise ValueError("Incorrect param")
#
#
# toyota = Car("camry", 123456)
# toyota.show_info()
#
# bmw = Car("x5", 321654)
# bmw.show_info()
#
# result = toyota + bmw
# print(result)
#
# result = toyota + 123
# print(result)

# дописать остальные операторы в классе Car
