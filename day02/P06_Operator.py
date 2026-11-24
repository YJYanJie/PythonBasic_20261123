"""
    演示了运算符
"""
"""
# 算术运算符
num1 = 10
num2 = 2
# +	加	a + b
print(num1 + num2)
# -	减、或取负	a - b、-a
print(num1 - num2)
# *	乘	a * b
print(num1 * num2)
# /	除	a / b
print(num1 / num2)
# //	整除，除后向下取整	a // b
print(num1 // num2)
# %	模，返回除法的余数	a % b
print(num1 % num2)
# **	幂	a ** b
print(num1 ** num2)
"""

"""
# 赋值运算符
# =	赋值
num1 = 10
# +=	加法赋值
# num1 += 1 # 等价于 num1 = num1 + 1
# -=	减法赋值
# num1 -= 1
# *=	乘法赋值
# num1 *= 2
# /=	除法赋值
# num1 /= 2
# //=	整除赋值
# num1 //= 2
# %=	模赋值
# num1 %= 3
# **=	幂赋值
# num1 **= 2
# print(num1)

# :=	海象运算符，在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增
# 一边赋值，一边返回这个值
num1 = 20
# TypeError: print() got an unexpected keyword argument 'num2', print 中没有 num2 关键字参数
# print((num2 := 30) > num1)
# print(num2)

# print(num2 := 30 > num1)
# print(num2)
"""

"""
# 比较运算符
# ==	相等，比较两者的值
# !=	不相等
# >	大于
# <	小于
# >=	大于等于
# <=	小于等于
# 比较运算符的返回结果是bool类型
num1 = 10
num2 = 20
print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)   # Flase
print(num1 < num2)   # True
print(num1 >= num2)  # False
print(num1 <= num2)  # True
num3 = 'abc'
# 注意：不同的数据类型之间不能进行大小的比较
# print(num1 > num3)
# 如果是字符串比较大小，是从最左边开始逐个比较字符串中相应位置的字符的ASCII码
print('5' > '6') # False
print('15' > '6') # False
"""

"""
# 逻辑运算符
b1 = True
b2 = False
# and	与，x and y，若x为False返回x的值，否则返回y的值
# print(b1 and b2)
# print(5 and 8)
# print(0 and 8)

# or	或，x or y，若x为True返回x的值，否则返回y的值
# print(b1 or b2)
# print(5 or 8)
# print(0 or 8)

# not	非，not x，若x为True返回False，若x为False返回True
# print(not b1)
print(not 5)
"""
"""
# 位运算符
# &	按位与
# |	按位或
# ^	按位异或
# ~	按位取反
# <<	按位左移
# >>	按位右移

# 成员运算符
# in 在指定的序列中找到值返回 True, 否则返回 Flase
# not in    在指定的序列中没有找到值返回 True, 否则返回 Flase

list1 = [1, 2, 3]
print(1 in list1)
print(11 not in list1)
"""
# 身份运算符
# is	判断两个标识符是不是引用自相同对象
# is not	判断两个标识符是不是引用自不同对象
m = 20
n = 20
q = 30
print(m is n)  # True 判断m和n在内存中是否指向同一个地址
print(n is q)  # False
print(n is not q)  # True
# id() 用于获取对象在内存中的地址
print(id(m) == id(n)) # True

print("-" * 30)
# -------------is 和 == 的区别---------------
a = [1,2,3]
b = a

print(b is a)  # True
print(b == a)  # True

b = a[:]
print(b)
print(b is a)  # False
print(b == a)  # True
