"""
    导入自定义的包中的模块内容
"""

"""
# 全局导入,包中某个模块下的所有成员
import graphic.circle
print(graphic.circle.PI)
import graphic.circle as c
print(c.PI)


import graphic
print(graphic.circle.PI)
# print(graphic.rectangle.rectangle_width)
"""

"""
# 局部导入 --1
# from 包名 import 模块名 [as 别名]   导入包中某一个模块的所有成员
from graphic import circle
print(circle.PI)
"""

"""
# 局部导入 --2
# from 包名.模块名 import 成员名 [as 别名]
from graphic.circle import PI, area
print(area(10))
print(PI)
print(perimeter(10))
"""

"""
# 局部导入 --3
# from 包名.模块名 import *  无法导入 _ 开头的成员
from graphic.circle import *
print(PI)
print(_str1)
"""

"""
# 局部导入 --4
# from 包名 import *  导入包中的所有模块
# 这种方式,需要在包下的 __init__.py 通过 __all__ 属性来控制哪些模块可以被导入
from graphic import *
print(circle.PI)
print(rectangle.rectangle_width)
"""


# from graphic import circle
# print(circle.PI)