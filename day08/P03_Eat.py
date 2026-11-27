"""
    模拟同学买蛋糕-分享-吃蛋糕
"""
class 学生:
    def __init__(self,姓名,年龄,性别):
        self.姓名 = 姓名
        self.__年龄 = 年龄
        self.性别 = 性别

    def 买(self,蛋糕):
        print(f"{self.姓名}买了一个{蛋糕.尺寸}的{蛋糕.材质}蛋糕")

    def 分享(self,std):
        print(f"{self.姓名}分享了一块蛋糕给{std.姓名},{std.姓名}很高兴")

    def 表达谢意(self):
        print(f"给所有的烦恼说拜拜，和所有快乐say HiHI")


class 蛋糕:
    def __init__(self,尺寸,材质,价格):
        self.尺寸 = 尺寸
        self.材质 = 材质
        self.__价格 = 价格

lbq = 学生("lbq",18,"女")

dg = 蛋糕("10寸","动物奶油",300)
lbq.买(dg)

wzb = 学生("wzb",28,"男")
lbq.分享(wzb)

wzb.表达谢意()

