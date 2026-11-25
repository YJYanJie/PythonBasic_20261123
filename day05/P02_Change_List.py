"""
    演示了防止函数修改列表
    需求:不希望在函数中,对原列表内容进行修改
"""
import copy

"""
# 浅拷贝
def change_list(list1):
    print(f"在函数中,修改列表前列表内容是{list1},地址的{id(list1)}")
    list1[1] = 20
    print(f"在函数中,修改列表后列表内容是{list1},地址的{id(list1)}")

list0 = [1, 2, 3]
print(f"在函数外,修改列表前列表内容是{list0},地址的{id(list0)}")
# change_list(list0)
list00 = list0.copy()
change_list(list00)
print(f"在函数外,修改列表后列表内容是{list0},地址的{id(list0)}")
"""
def change_list(list1):
    print(f"在函数中,修改列表前列表内容是{list1},地址的{id(list1)}")
    list1[3].append(40)
    print(f"在函数中,修改列表后列表内容是{list1},地址的{id(list1)}")

list0 = [1, 2, 3, [10, 20, 30]]
print(f"在函数外,修改列表前列表内容是{list0},地址的{id(list0)}")
list00 = list0.copy() # 浅拷贝
list00 = list0[:]
list00 = copy.deepcopy(list0) # 深拷贝
change_list(list00)
print(f"在函数外,修改列表后列表内容是{list0},地址的{id(list0)}")
