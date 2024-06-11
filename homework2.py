# Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# Створіть клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові, мобільний телефон і т.д.
# Створіть клас "Замовлення". Замовлення може містити кілька товарів,
# причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.
class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} UAH, Description: {self.description}, Dimensions: {self.dimensions}"

class Customer:
    def __init__(self, last_name, first_name, middle_name, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"Покупателя: {self.last_name} {self.first_name} {self.middle_name}, Моб: {self.phone}"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def total_price(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

    def __str__(self):
        products_str = "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items])
        return f"Заказ {self.customer}:\n{products_str}\nСумма за всё: {self.total_price()} ГРН"

# Створення екземплярів класів Product
product1 = Product(name="MacBook m1", price=15000, description="Programing laptop", dimensions="35x25x2 cm")
product2 = Product(name="Mouse Razer", price=500, description="Wireless mouse", dimensions="10x5x3 cm")
product3 = Product(name="SmartMonitor m7", price=9500, description="Monitor for work", dimensions="105x54x3 cm")
product4 = Product(name="Зарядная станция", price=20000, description="PowerPlant", dimensions="105x504x3 cm")

# Створення екземпляра класу Customer
customer = Customer(last_name="Барило", first_name="Радион", middle_name="Петрович", phone="380637685508")

# Створення екземпляра класу Order
order = Order(customer)

# Додавання товарів до замовлення
order.add_product(product1, 1)
order.add_product(product2, 2)
order.add_product(product3, 1)
order.add_product(product4, 3)

# Виведення інформації про замовлення
print(order)
