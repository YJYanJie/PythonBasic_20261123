"""
    演示了双分支
    需求：
    余额随机，商品价格50。
    	若余额小于50则提示“余额不足，请充值”。
    	否则提示消费成功。
    最后打印“欢迎下次光临”。
"""
price = 50

from random import randint

balance = randint(0, 100)
print(f"原来余额:{balance}")

if balance < price:
    print("余额不足，请充值")
else:
    balance -= price
    print(f"消费成功,还剩{balance}")

print("欢迎下次光临")