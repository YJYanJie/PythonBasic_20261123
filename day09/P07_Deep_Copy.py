"""
    演示了浅拷贝和深拷贝
"""
"""
import copy
list1 = [1, 2, 3]

# 以下四种方式实现的是浅拷贝
# list2 = list1[:]
# list2 = list1.copy()
# list2 = list(list1)
list2 = copy.copy(list1)
print(id(list1), id(list2))

# 深拷贝
list2 = copy.deepcopy(list1)
print(id(list1), id(list2))
"""


"""
import copy

list1 = [1, 2, 3, [100, 200, 300]]
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)

# 浅拷贝只拷贝最外层对象,那么 list1[3] 和 list2[3] 的地址是一样的
# list2 = copy.copy(list1)
# 深拷贝是每一层都会进行拷贝,那么 list1[3] 和 list2[3] 的地址是不一样的
list2 = copy.deepcopy(list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)


print("~~~~~~~")
list1[0] = 100
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)


# list1[3].append(400)  # 修改list1[3]列表元素，向列表中添加新值
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)
"""

"""
# 非容器类型（如数字、字符串、和其他“原子”类型的对象）无法拷贝
import copy

var1 = 1
print(id(var1), var1)

var2 = copy.copy(var1)
print(id(var2), var2)

var3 = copy.deepcopy(var1)
print(id(var3), var3)
"""

# 元组变量如果只包含原子类型对象，则不能对其深拷贝
import copy

tuple1 = (1, 2, 3)  # 元组只包含原子类型对象
# tuple1 = (1, 2, 3,[])  # 元组中包含了可变类型对象
print(id(tuple1), tuple1)

# 浅拷贝
# tuple2 = tuple1[:]
# 深拷贝
tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2)
