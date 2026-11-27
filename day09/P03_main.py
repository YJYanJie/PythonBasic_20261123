"""
    导入模块的方式
"""
"""
# 导入自己创建的 P02_my_add 模块,并使用其成员

# 全局导入 通过 模块名.成员名
import P02_my_add

print(P02_my_add.num)
print(P02_my_add.add(1, 2))


# 全局导入,起别名, 通过 别名.成员名 的方式访问
import P02_my_add as a1

print(a1.num)
print(a1.add(1, 2))
"""

"""
# 局部导入, 导入模块的部分成员,直接通过成员名的方式访问
from P02_my_add import add
print(add(1, 2))
# 只能使用导入的成员,未导入的成员无法使用
# print(num)


# 如果导入的成员有重名，后导入的成员会将前面的导入成员覆盖掉
from P04_my_multi import multi, num
from P02_my_add import add, num
print(add(1, 2))
print(multi(1, 2))
print(num)


# 可以通过别名来区分重名的成员
from P04_my_multi import multi, num as n1
from P02_my_add import add, num as n2
print(add(1,2))
print(multi(2,3))
print(n1)
print(n2)
# 只能使用别名的方式访问成员了
# print(num)


# 局部导入2 导入模块中所有不以单下划线开头的成员
# import P04_my_multi as mymulti
# print(mymulti._str1)

# from P04_my_multi import _str1
# print(_str1)

from P04_my_multi import *
print(num)
print(multi(2,3))
# print(_str1) 访问不了 _str1
"""

"""
# 模块的搜索顺序
import sys
print(sys.version)
print(sys.path)
sys.path.append("./..")
print(sys.path)
# import time
# time.sleep(3)
# print("end")
"""

"""
# __slots__ 限制类的实例能够添加的实例属性和实例方法,但是只对本类生效,子类不生效
# __all__ 限制被导入成员, 只针对 from 模块 import * 时有效

# 全局导入
import P02_my_add
print(P02_my_add.num)
print(P02_my_add.add(1, 2))
print(P02_my_add.num1)
print(P02_my_add._str1)

from P02_my_add import num
from P02_my_add import num1
from P02_my_add import _str1
from P02_my_add import add
print(num)
print(num1)
print(_str1)
print(add(1,2))


from P02_my_add import *
print(_str1)
print(num)
# print(num1)
"""

# __name__ 属性
import P02_my_add
# from P02_my_add import add
# from P02_my_add import *