"""
    演示了私有化
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        # 约定: 当前属性是不想被暴露的,这种私有化方式不具备强制约束性
        self._age = age
        self.__age = age  # 底层使用的改名的方式,实现的私有化. __x ==> _类名__x

    # 私有化方法
    def __private_method(self):
        print("private method")

p1 = Person("zsh", 20)
print(p1.name)
# print(p1._age)
# print(p1.__age)
# 访问私有化属性
print(p1._Person__age)

# 访问私有化方法
p1._Person__private_method()