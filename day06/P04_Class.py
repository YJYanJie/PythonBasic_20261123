"""
    演示了类的定义
"""
class Person:
    """人的类"""

    # 属性 -- 类属性(所有类创建出来的对象共用)
    home = "earth"

    # 方法
    def __init__(self, name, age):
        # 属性 -- 实例方法(每个类创建出来的对象独有)
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

    def drink(self):
        print("drinking")

# 类的操作 --- 实例化
zs = Person("zs", 20)
zs.eat()
print(zs.name)

# 类的操作 --- 成员引用: 通过类名来调用类的方法或属性
home = Person.home
eat_func = Person.eat
drink_func = Person.drink
doc = Person.__doc__
print(home)
print(eat_func)
print(drink_func)
print(doc)
