"""
    演示了数据类型
"""
# num1 = 10
# type() 查看变量类型
# print(type(num1))

# num1 = 1_000_000_000_000_000
# print(num1)  # 1000000000000000

# num2 = True
# print(num2, type(num2))

# print(type(num1) == type(num2))

# type() 和 isinstance() 的区别在于 type() 不会认为子类是一种父类类型，isinstance() 会认为子类是一种父类类型。
# print(isinstance(num1, int))
# print(isinstance(num2, bool))
# print(isinstance(num2, int))

num1 = 10
num2 = 10
print(num1, num2)
print(type(num1), type(num2))
# id() 用于获取对象在内存中的地址
print(id(num1), id(num2))

num3 = 300
num4 = 300
print(id(num3), id(num4))

# 小整数池：[-5, 256] 的整数维护在小整数对象池中，这些整数都是提前创建好的，不会被垃圾回收，避免了为整数频繁申请和销毁内存空间。
# 大整数池：一开始大整数池为空，每创建一个大整数就会向池中存储一个。
#       注意事项：小整数池的范围和实现细节不同， Python 解释器实现方式不同