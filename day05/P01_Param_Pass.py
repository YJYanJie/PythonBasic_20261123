"""
    演示了函数参数传递的形式
"""
"""
# 必须参数(按照参数的位置进行匹配)
def print_info(a, b, c):
    print(a, b, c)

print_info(2,1,3)


# 关键字参数(按照参数的名称进行匹配)
def print_info(name, age):
    print(name)
    print(age)

# print_info("zs", 20)
print_info(name="zs", age=20)
print_info(age=20, name="zs")


# 默认值参数
# def print_info(name,age):
def print_info(name,age='18'):
    print(name,age)

print_info(name="zs")
print_info("as")
print_info(name='lis',age=30)


# 不定长参数(可变长参数) 形式1:  *参数名
# print(1, 2, 3)
def print_info(name, *args, age):
    print(name, args, age, type(args))

print_info("zs", 1, 2, 3, 4, 5, 6, age=19)
print_info("zs", 2, age=20)

def print_info(name, **args):
    print(name, args)

print_info("zs", a=1, b=2, c=3)


# 解包传参
def func(a, b, c):
    print(a, b, c)

func(1, 2, 3)
func(a=1, b=2, c=3)

tup1 = (1, 2, 3)
func(*tup1)

dict1 = {'a':1,'b':2,'c':3}
func(**dict1)
"""

# 强制使用位置参数或者关键字参数   /前必须使用位置传参, * 后的参数必须用关键字传参
def func(a, b, /, c, d, e, *, f, g):
    print(a, b, c, d, e, f, g)

func(1, 2, 3, 4, 5, f=6, g=7)