"""
    演示了异常传递
"""
"""
# 情况1: try 块的嵌套
try:
    try:

        try:
            print(1 / 0)
        except TypeError:
            print("第三层")

    except NameError as e:
        print("第二层")
        
except:
    print("第一层")
"""

# 函数传递
def m3():
    print(1/0)

def m2():
    m3()

def m1():
    m2()

# 函数调用的顺序 m1->m2->m3
m1()