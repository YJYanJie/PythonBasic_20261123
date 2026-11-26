"""
    演示了类属性
"""
class Person:
    """人的类"""
    home = "earth"


# 通过 类名.属性名 方式访问
# print(Person.home)

# 通过 实例名.属性名 方式访问
# zs = Person()
# print(zs.home)
#
# ls = Person()
# print(ls.home)

# 通过 类名.属性名 方式修改|添加
# print(Person.home)
# Person.home = "地球"
# print(Person.home)


zs = Person()
zs.home = "地球"
print(zs.home)

ls = Person()
print(ls.home)
