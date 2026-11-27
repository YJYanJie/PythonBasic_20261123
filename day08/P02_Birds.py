"""
    演示了愤怒的小鸟
"""
class Birds:
    def __init__(self, name, color, skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description

    def fly(self):
        pass

    def call(self):
        pass

    def use_skill(self):
        print(f"{self.name}使用了技能:{self.skill_description}")

class RedBirds(Birds):
    def __init__(self, name, color, skill_description):
        super().__init__(name, color, skill_description)

    def fly(self):
        print("红鸟以稳定的速度飞行")

    def call(self):
        print("红火发出 'wei呀....' 的叫声")

class YellowBirds(Birds):
    def __init__(self, name, color, skill_description):
        super().__init__(name, color, skill_description)

    def fly(self):
        print("黄鸟快速飞行")

    def call(self):
        print("黄蜂发出了喳喳...的叫声")


class BlueBirds(Birds):
    def __init__(self, name, color, skill_description):
        super().__init__(name, color, skill_description)

    def fly(self):
        print("蓝鸟优雅的飞行")

    def call(self):
        print("蓝冰发出了啾啾...的叫声")


class Obstacle():
    """障碍物类"""
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def be_attacked(self, bird):
        print(f"{bird.name}向障碍物{self.name}发起了攻击")
        bird.use_skill()

        # 不同鸟类的攻击伤害不同
        if isinstance(bird, RedBirds):
            damage = 50
        elif isinstance(bird, YellowBirds):
            damage = 80
        else:
            damage = 30 * 3

        self.strength -= damage
        # 判断障碍物是否被销毁
        if self.strength <= 0:
            print(f"障碍物{self.name}被摧毁了")
        else:
            print(f"障碍物{self.name}受到攻击，还有{self.strength}生命值")


# 创建一个障碍物
o1 = Obstacle("石头房子", 100)

# 红鸟
r1 = RedBirds("小红", "红色", "红鸟攻击")
o1.be_attacked(r1)

print("-" * 30)
# 黄鸟
y1 = YellowBirds("小黄", "黄色", "黄鸟攻击")
o1.be_attacked(y1)