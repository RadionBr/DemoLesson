# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого
# складається з обєктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.)
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
#
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
#
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.

# ДЗ 14.1. Виняток користувача
# Модифікуйте клас Група (завдання минулої лекції) так,
# щоб при спробі додавання до групи більше 10-ти студентів, було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Human: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}, Record Book: {self.record_book}'

class GroupFullException(Exception):
    pass

class Group:
    def __init__(self, number, students_limit=10):
        self.number = number
        self.group = set()
        self.students_limit = students_limit

    def add_student(self, student):
        if len(self.group) >= self.students_limit:
            raise GroupFullException(f'Cannot add student: group {self.number} is full')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'

# Test code
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'Mark', 'Zuckerberg', 'AN150')
st4 = Student('Female', 23, 'Ada', 'Lovelace', 'AN151')
st5 = Student('Male', 24, 'Bill', 'Gates', 'AN152')
st6 = Student('Female', 21, 'Grace', 'Hopper', 'AN153')
st7 = Student('Male', 25, 'Elon', 'Musk', 'AN154')
st8 = Student('Female', 20, 'Margaret', 'Hamilton', 'AN155')
st9 = Student('Male', 27, 'Larry', 'Page', 'AN156')
st10 = Student('Female', 28, 'Sergey', 'Brin', 'AN157')
st11 = Student('Male', 29, 'Jeff', 'Bezos', 'AN158')

gr = Group('PD1', students_limit=10)
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

print(gr)

try:
    gr.add_student(st11)
except GroupFullException as e:
    print(e)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only nine students

gr.delete_student('Taylor')  # No error!

