"""
    演示了raise关键字
"""
# 两个整数的加法运算
def add(num1, num2):
    # if isinstance(num1, int) and isinstance(num2, int):
    #     return num1 + num2
    # else:
    #     # 抛出异常
    #     raise TypeError("参数类型必须为整数")
    assert isinstance(num1, int) and isinstance(num2, int) , "参数类型必须为整数"
    return num1 + num2

# print(add(1.0, 2))

try:
    res = add(1.0, 2)
except (TypeError, AssertionError) as e:
    print(e)
else:
    print(res)

print("end")