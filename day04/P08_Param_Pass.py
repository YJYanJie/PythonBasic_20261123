"""
    参数的传递
"""
"""
# 传递不可变类型数据
def change_int(a):
    print(f"在函数体中,修改前a的值{a},地址是{id(a)}")
    a = 10
    print(f"在函数体中,修改后a的值{a},地址是{id(a)}")

b = 2
print(f"在函数体外,修改前b的值{b},地址是{id(b)}")
change_int(b)
print(f"在函数体外,修改后b的值{b},地址是{id(b)}")
"""

# 传递可变类型数据
def change_list(list1):
    print(f"在函数体中,修改前a的值{list1},地址是{id(list1)}")
    # list1[2] = 10
    # list1 = list1 * 2 # 创建了一个新的对象
    list1 *= 2 # 未创建新的对象
    print(f"在函数体中,修改后a的值{list1},地址是{id(list1)}")

list0 = [1, 2, 3]
print(f"在函数体外,修改前b的值{list0},地址是{id(list0)}")
change_list(list0)
print(f"在函数体外,修改后b的值{list0},地址是{id(list0)}")
