"""
    演示了面向过程,面向对象以及面向函数式编程范式
    东北大拉皮
    锅包肉
    东北大乱炖
"""
"""
# ~~~~~~~~~~面向过程~~~~~~~~~~~~
def 洗(name):
    print(f"洗{name}")

def 切(name):
    print(f"切{name}")

def 拌(*name):
    print(f"拌{name}")

def 上菜(name):
    print(f"{name}上桌~~~")

def 炸(name):
    print(f"炸{name}")

def 炖(*name):
    print(f"炖{name}")


洗("黄瓜")
切("黄瓜")
拌("黄瓜","拉皮")
上菜("东北大拉皮")

洗("肉")
炸("肉")
上菜("锅包肉")

洗("茄子")
洗("豆角")
洗("土豆")
切("茄子")
切("土豆")
炖("茄子","豆角","土豆","排骨")
上菜("东北大乱炖")
"""

"""
# ~~~~~~~~~~面向对象~~~~~~~~~~~~
class 菜:
    def __init__(self, name):
        self.name = name

    def 洗(self, czn):
        print(f"洗{czn}")

    def 切(self, czn):
        print(f"切{czn}")

    def 拌(self, *czn):
        print(f"拌{czn}")

    def 上菜(self):
        print(f"{self.name}上桌~~~")

    def 炸(self, czn):
        print(f"炸{czn}")

    def 炖(self, *czn):
        print(f"炖{czn}")

dlp = 菜("东北大拉皮")
dlp.洗("黄瓜")
dlp.切("黄瓜")
dlp.拌("黄瓜","拉皮")
dlp.上菜()
"""

# ~~~~~~~~~~面向函数~~~~~~~~~~~~
# list1 = [1,2,3]
# map(lambda item:"1234->" + str(item), list1)
# def outer():
#     a = 10
#     def inner():
#         print(a)
#     return inner

def 洗黄瓜():
    print("洗黄瓜")
def 切黄瓜():
    print("切黄瓜")
def 拌():
    print("将黄瓜和拉皮搅拌")
def 上菜():
    print("大拉皮上桌")

def 东北大拉皮(*funcs):
    for func in funcs:
        func()

东北大拉皮(洗黄瓜,切黄瓜,拌,上菜)
