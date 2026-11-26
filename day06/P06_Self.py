"""
    演示了self
"""
class Student:
    # 类属性
    school = "school"

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

    def 站着听(self):
        self.eat()

xs = Student("xs", 19)
xs.eat()
print(xs.name)
print(xs.age)
xs.站着听()  # ===>Student.站着听(xjq)
print(id(xs.站着听()))
print(id(Student.站着听(xs)))