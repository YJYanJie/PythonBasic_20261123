"""
    演示了多态
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.age}岁的{self.name}去吃饭了")


class Teacher(Person):
    pass


class Student(Person):
    pass


def 放学吃饭(person):
    person.eat()

# 同一个对象,不同的表现形式
tea = Teacher("tea", 18)
放学吃饭(tea)

xjq = Student("xjq",20)
放学吃饭(xjq)


# new_obj 封装对象创建逻辑，按需产出不同子类实例
# 返回值的多态
def new_obj(num):
    if num == 1:
        obj = Teacher("fxf",18)
    else:
        obj = Student("xjq",20)

    return obj

# obj = new_obj(1)
obj = new_obj(2)
print(obj.name, obj.age)