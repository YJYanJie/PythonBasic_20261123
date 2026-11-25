"""
    演示了函数的嵌套调用
"""
def func_a():
    print('func_a开始执行')
    func_b()
    print('func_a执行结束')



def func_b():
    print('func_b开始执行')
    print('func_b执行结束')

func_a()