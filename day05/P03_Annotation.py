"""
    演示了函数说明文档
"""
def adult(age):
    """该函数判断是否成年"""
    return "成年" if age >10 else "未成年"

# 可以通过 help(函数名) 获取函数说明文档
help(adult)