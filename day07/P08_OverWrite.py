"""
    演示了方法的重写
"""
"""
class Person:
    def eat(self):
        print("person eat")


class Student(Person):
    pass
    # def eat(self):
    #     print("student eat")

s = Student()
s.eat()
"""

"""
class Person:
    def eat(self, a, b):
        print("person eat")


class Student(Person):
    # pass
    
    def eat(self, a, b):
        print("student eat")
        
    # python中没有重载,因此下面的 eat() 方法会将继承父类的方法覆盖掉
    def eat(self, a):
        print("student eat")
    

print(Student.__mro__)
s = Student()
s.eat(1, 2)
"""

class Person:
    def eat(self,a):
        print("person eat")

class Student(Person):
    def eat(self, a, b):
        # Person.eat(self,a)
        # super().eat(a)
        # self.eat(a)
        print("Student eat")


print(Student.__mro__)
s = Student()
s.eat(10,20)