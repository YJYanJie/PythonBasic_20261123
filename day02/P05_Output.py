"""
    演示了 print 函数的格式化输出操作
"""

"""
# 直接使用 print 进行打印输出
# print("Hello World")

# 通过 print 输出多个值,多个值之间,使用逗号分隔
# print("Hello World", "Hello Python", "World")

# 使用 end= 来控制 print() 以什么结尾
print("hello", end=" ")
print("world")
"""

"""
# 格式化输出
# 1. 字符串中使用 % 占位
int1 = 10
float1 = 3.23
str1 = "int1=%d,float1=%f" % (int1, float1)
print(str1)

# 2. 字符串.format()
# 方式1: 不设置指定位置,按默认顺序
int1 = 10
float1 = 3.23
bool1 = True
str1 = "int1={}, float1={}, bool1={}".format(int1, float1, bool1)
print(str1)

# 方式2: 设置指定位置,不能和方式1混合使用
int1 = 10
float1 = 3.23
bool1 = True
str1 = "int1={0}, float1={0}, bool1={2}".format(int1, float1, bool1)
print(str1)

# 方式3: 设置参数
int1 = 10
float1 = 3.23
bool1 = True
str1 = "int1={a}, float1={b}, bool1={c}".format(a=int1, b=float1, c=bool1)
print(str1)

# 3. 数字格式化
# * 指定填充字符
# ^ 居中  < 居左    > 居右
# 指定输出20个字符,如果不够,用指定的填充符号进行填充,默认是空格
# ,或者_  数字每3位进行分隔
# .2f   保留两位小数
float1 = 31415.9
str2 = "{:*^20,.2f}".format(float1)
print(str2)
"""
# 5. f-字符串格式化输出
int1 = 10
float1 = 3.23
bool1 = True
str1 = f"int1={int1}, float1={float1}"
str1 = f"{int1 = }, {float1 = }"
# {} 外再嵌套一层 {}, 会进行转义
str1 = f"{{int1=}}, {float1=}"
print(str1)