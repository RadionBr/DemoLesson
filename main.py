from student import Student
from group import Group
from exceptions import GroupFullException

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

assert gr.find_student('Jobs') == st1, 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only nine students

gr.delete_student('Taylor')  # No error!
