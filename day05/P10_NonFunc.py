"""
    演示了匿名函数
    需求:定义一个计算器,完成两个数的加, 减, 乘, 除运算
"""
"""
def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
print(calculate(10, 20, '*'))
"""
"""
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def calculate(num1, num2, op):
    return op(num1, num2)

print(calculate(10, 20, add))
print(calculate(10, 20, sub))
print(calculate(10, 20, mul))
"""

"""
# 匿名函数实现
def calculate(num1, num2, op):
    return op(num1, num2)

print(calculate(10, 20, lambda a, b: a + b))
"""
"""
# 匿名函数作为内置函数的参数
student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]

# sorted 排序
print(sorted(student_list, key=lambda std_dict: std_dict["age"], reverse=True))

# map 对序列中的元素逐一处理
list1 = [i for i in range(5)]
def op(item):
    return "2026-11-25 -> " + str(item)
print(list(map(lambda item: "2026-11-25 -> " + str(item), list1)))

# filter 对序列中的元素进行过滤
list1 = [i for i in range(10) if i % 2 == 0]
list1 = [i for i in range(10)]
print(list(filter(lambda item: item % 2 == 0, list1)))

# reduce 对序列中元素进行累积
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
"""

"""
# 没有匿名函数时
list1 = [i for i in range(5)]

# def func(list1):
#     list2 = []
#     for item in list1:
#         list2.append("2026-11-25 -> " + str(item))
#     return list2
# print(func(list1))

def my_func(item):
    return "2026-11-25 -> " + str(item)

def my_map(func, list1):
    list2 = []
    for item in list1:
        list2.append(func(item))
    return list2

# print(my_map(my_func, list1))
print(my_map(lambda x : x * 2, list1))
"""

# 函数的注释
# 普通的自定义函数:
# def dog(name, age, specices):
#     return (name, age, specices)

def dog(name:str='wc', age:(1, 99)=22, species:'狗狗的品种'='za') -> tuple:
    return (name, age, species)

print(dog(11, 200, 'xxx'))
print(dog.__annotations__)