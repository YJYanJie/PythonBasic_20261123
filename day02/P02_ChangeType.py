"""
    演示了类型转换
"""
"""
# 隐式类型转换: 对两种不同的数据类型进行运算,较小的数据类型会被转换为较大的数据类型,以避免数据丢失
num1 = 10
num2 = 15.5
print(type(num1), type(num2))
num3 = num1 + num2
print(num3, type(num3))

# 特别的,两个整数进行除法运算结果也是浮点数
num4 = 4
num5 = 2
num6 = num4 / num5
print(num6, type(num6))

# 整型和字符串相加会报错,此时Python无法进行隐式转换完成计算
age = 18
print("年龄为:" + age) # Java 中属于字符串拼接, Python中则不允许这种操作,除非使用 str() 强制转换
"""

# 强制类型转换
# int(x [,base])	将x转换为一个整数，x若为字符串可用base指定进制
# var1 = int("1010", base=2)
# print(var1, type(var1))

# float(x)	将x转换为一个浮点数
# var1 = float("12.33")
# print(var1, type(var1))

# complex(real[,imag])	创建一个实部为real，虚部为imag的复数
# print(complex(3, 5)) # 3 + 5j

# 类中的魔法方法
# str(x)	将对象x转换为一个字符串
# repr(x)	将对象x转换为一个字符串，可以转义字符串中的特殊字符

# eval(x)	执行x字符串表达式，并返回表达式的值
# eval("print(123)")

# bin(x)	将一个整数转换为一个二进制字符串
# oct(x)	将一个整数转换为一个八进制字符串
# hex(x)	将一个整数转换为一个十六进制字符串

# ord(x)	将一个字符转换为它的ASCII整数值
print(ord("a"))
# chr(x)	将一个整数转换为一个Unicode字符
print(chr(65))

# tuple(s)	将序列s转换为一个元组
# list(s)	将序列s转换为一个列表
# set(s)	转换s为可变集合
