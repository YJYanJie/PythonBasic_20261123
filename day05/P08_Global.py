"""
    演示了全局变量以及局部变量和 global、nonlocal关键字
"""
"""
# 全局变量和局部变量
# 全局变量: 定义在模块下,函数外.可以被当前模块的所有内容访问
# 局部变量: 定义在函数内,只能被当前函数访问
# 如果局部变量和全局变量名字相同,局部优先

# 全局变量
var0 = 10

def func_1():
    var1 = 20
    # 在函数体中, 可以访问全局变量
    print(var0)
    # 在函数体中, 可以访问自己定义的局部变量
    print(var1)

def func_2():
    var2 = 30
    # 在函数体中, 可以访问全局变量
    print(var0)
    # 在函数体中, 可以访问自己定义的局部变量
    print(var2)
    
func_1()
func_2()
"""
"""
var1 = 10
def func():
    # 如果在函数体中,对变量进行赋值操作,python会将变量当作局部变量进行处理
    # 哪怕存在着同名的全局变量
    # 如果当作局部变量进行处理,那么 var1 需要先被定义
    # var1 = 100
    # var1 += 1 # var1 = var1 + 1
    # var1 = var1 + 1
    print(var1)
func()
"""
"""
var1 = 10
def func():
    # 在函数体中修改的局部变量,和全局变量没有关系
    var1 = 20
    print(var1)
func()
print(var1)
"""
"""
# 如果在函数体中,想要对全局变量做修改
var1 = 10
def func():
    # 声明当前在函数体中操作的变量,就是全局变量,这个时候,就不会再单独创建局部变量了
    global var1
    var1 = 20
    print(var1)
func()
print(var1)
"""
"""
# 修改可变类型的全局变量
var1 = [1, 2, 3]
def func():
    # 严格讲,下面操作不算是赋值,算是修改,操作的还是全局变量
    # var1[1] = 20

    # 下面操作属于赋值操作,会创建一个局部变量 var1
    # global var1
    # var1 = [2, 3, 4]
    var1[:] = [2, 3, 4]
    print(var1)
func()
print(var1)
"""

def outer():
    var1 = 10
    def inner():
        nonlocal var1
        var1 = 20
        print(var1)
    inner()
    print(var1)

outer()