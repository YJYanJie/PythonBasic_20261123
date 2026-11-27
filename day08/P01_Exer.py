"""
    练习
"""

"""
# 题目 1：动态添加属性
# 定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。
class Person:
    pass

p1 = Person()
p1.hobby = "reading"
print(p1.hobby)
"""

"""
# 题目 2：动态添加方法
# 定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：\\(S = π r^2），
# 然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用 types.MethodType）

import types

class Circle:
    def __init__(self, radius):
        self.radius = radius

def calculate_area(self):
    return 3.14 * self.radius ** 2

c1 = Circle(5)
c1.calculate_area = types.MethodType(calculate_area, c1)
print(c1.calculate_area())
"""

"""
# 题目 3：封装特性
# 定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），提供一个 deposit 方法用于存钱，一个 withdraw 方法用于取钱，
# 取钱时如果余额不足则打印提示信息。

class BandAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入{amount}元，当前余额为{self.__balance}元")
        else:
            print("存入金额需大于0")

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"取出{amount}元，当前余额为{self.__balance}元")
        else:
            print("余额不足或取出金额不合法")
"""

"""
# 题目 4：多态特性
# 定义一个 Shape 类，有一个抽象方法 area（方法体为空）。再定义 Rectangle 类和 Circle 类继承自 Shape 类，分别实现 area 方法计算
# 矩形面积（长 × 宽）和圆的面积（\(\pi r^2\)）。创建 Rectangle 和 Circle 类的对象，将它们放入一个列表中，遍历列表并调用每个对
# 象的 area 方法。
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())
"""