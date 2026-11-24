"""
    演示了数据类型
"""
"""
# 浮点数类型
f1 = 0.1
f2 = 0.2

# 在任何编程语言中,浮点数类型都存在精度丢失的情况
f3 = f1 + f2
print(f3, type(f3))

from decimal import Decimal
f1 = Decimal("0.1")
f2 = Decimal("0.2")
f3 = f1 + f2
print(f3, type(f3))
"""

""""
# bool 布尔类型
bool1 = True
bool2 = False
print(bool1, type(bool1))

# Python3 中, bool 是 int 的子类, True 和 False 可以和数字相加
print(isinstance(bool1, bool))
print(isinstance(bool1, int))

print(bool1 + 10) # 11
print(bool2 + 10) # 10

print("~" * 20)
print(bool1 == 1) # True

print(bool1 is 1) # False


bool1 = True
num = 1

print(bool1 == num)
print(bool1 is num)

# 在 Python 中,能够解释为假的值不只有 False,还有:None, 0.0, 0, False, 所有空容器(空列表, 空元组, 空集合, 空字典, 空字符串)
"""

# 字符串类型
# 可以用单引号括起来
# str1 = 'hello'
# print(str1, type(str1))

# 可以用双引号括起来
# str2 = "world"
# print(str2, type(str2))

# 可以使用三个引号括起来,将字符串原样输出
# str3 = ("""hello
# world""")
# print(str3, type(str3))

# str4 = ("hello \
# world")
# print(str4, type(str4))

# 常用的转义字符
# \: 转义符号 | 续行符
# \b    退格
# \n    换行
# \t    横向制表符
# \r    回车,回到行首
# str5 = "hello\rworld"
# print(str5, type(str5))

# intern 机制: 每个字符串,不夹杂空格或者特殊符号,默认开启 intern 机制,共享内存,靠引用计数来决定是否销毁. 相同的字符串默认只保留一份,当创建
#             一个字符串,它会先检查内存里有没有这个字符串,如果有就不再创建新的了.
# 字符串缓冲池: 单个字母,长度为 1 的 ASCII 字符会被 interned, 包括空字符
str6 = "hello world"
str7 = "hello world"
print(id(str6), id(str7))