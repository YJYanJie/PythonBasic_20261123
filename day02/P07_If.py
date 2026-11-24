"""
    演示了if单分支
    需求：商品价格50，若余额小于50则提示“余额不足，请充值”，最后打印“欢迎下次光临”
"""
#商品价格
price = 50

# 获取余额
# balance = input("请输入余额")

# 随机生成余额
from random import randint

balance = randint(0, 100)
print(f"余额是{balance}")

# 判断余额是不是小于商品价格
if balance < price :
    print("余额不足，请充值")

print("欢迎下次光临")