"""
    演示了字典
"""

# 创建字典对象
# dict1 = {"key1":"value1", "key2":"value2"}
# dict2 = {}
# dict2 = dict()
# print(dict1, type(dict1))
# print(dict2, type(dict2))
# dict1 = dict(name="zs", age=18)
# dict1 = dict([("name", "Tom"), ("age", 22), ("gender", "male")])
# print(dict1)
# 字典推导式
# dic = {i:i*2 for i in range(5)}
# print(dic, type(dic))

# 访问字典中元素
dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# print(dict1)
# print(dict1["name"])
# print(dict1["age"])
# print(dict1["gender"])
# 如果key不存在,那么直接报错
# print(dict1["address"])

# print(dict1.get("name"))
# 如果key不存在,返回None,不会报错
# print(dict1.get("address"))

# print(dict1)
# 向字典中添加元素
# dict1["address"] = "北京"

# 修改字典中元素
# dict1["age"] = 20

# 判断key是不是字典的成员
# 注意:只能对key进行判断,不能对value进行判断
# print("Alice" in dict1)

# 获取字典长度
# print(len(dict1))


# 删除字典中元素
# print(dict1)
# dict1.pop("name")
# del dict1["age"]
# del dict1
# print(dict1)


# 字典中常用方法 --- 对字典如何进行遍历
dict1 = {"唐僧":"迟重瑞","悟空":"六小龄童","八戒":"马德华","沙和尚":"闫怀礼"}
print(dict1)
dict1["长春悟空"] = "六小龄童"
print(dict1)

# 遍历所有key
# keys = dict1.keys()
# print(keys, type(keys))
# for key in keys:
#     print(key)

# 遍历所有 value
# values = dict1.values()
# for v in values:
#     print(v)


# 遍历 k-v 键值对
# for k in dict1.keys():
#     print(k, dict1[k])

for k,v in dict1.items():
    print(k,v)



# del dict[key]	根据key删除键值对
# dict.pop(key[,default])	获取key所对应的value，同时删除该键值对，可设置默认值
# dict.popitem()	取出字典中的最后插入的键值对，字典为空则报错
# dict.clear()	清空字典
# dict1.update(dict2)	将dict2中的键值对更新到dict1中
# dict.get(key[,default])	获取字典中key对应value，可设置默认值
# dict.setdefault(key[,default])	获取字典中key对应value，可设置默认值。若key不存在于字典中，将会添加key并将value设为默认值
# dict.keys()	获取字典所有的key，返回一个视图对象。字典改变，视图也会跟着变化
# dict.values()	获取字典所有的value，返回一个视图对象
# dict.items()	获取字典所有的(key,value)，返回一个视图对象
# dict.copy()	拷贝字典
# dict.fromkeys(seq[,default])	以序列seq中元素做字典的key创建一个新字典，可设置value的默认值
