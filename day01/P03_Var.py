"""
    演示了变量
"""
# a = 10
# b = 20
# print(a)
# print(b)


# var1 = 10
# var2 = 20
# var3 = var1 + var2
# print(var3)
#
# name = "zhagnsan"
# age = 18
# weight = 80.5
#
# print(name, age, weight)

# 定义多个变量
# n1 = 10
# n2 = 10
# n3 = 10
# n1 = n2 = n3 = 20

# n1 = 10
# n2 = 10
# n3 = 10
# n1, n2, n3 = 10, 20, 30
# print(n1, n2, n3)

# 标识符命名方式
# 大驼峰：ZhangSanFeng
# 小驼峰：zhangSanFeng
# 蛇形命名法：zhang_san_feng

# Python 中的关键字
import keyword
print(keyword.kwlist)

# 变量的修改
# msg = "hello"
# print(msg)
# msg = "world"
# print(msg)

var1,var2 = 10,20
print(var1,var2)

# temp = var1
# var1 = var2
# var2 = temp
# print(var1,var2)

var1,var2 = var2, var1

print(var1,var2)