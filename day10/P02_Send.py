"""
    演示了 send 向生成器函数发生值
"""
# 使用 send() 发送任务 id,使生成交替执行两个任务
def gen():
    task_id = 0
    int_value = 0
    char_value = 'A'
    while True:
        match task_id:
            case 0:
                # send 函数发送的数据,会作为 yield 表达式的返回值, 赋值给 task_id
                task_id = yield int_value # 返回 int_value, 并接收 send() 发送的值给 task_id
                int_value += 1
                print(f"task_id:{task_id}")
                print(f"int_value:{int_value}")
            case 1:
                task_id = yield char_value # 返回 char_value, 并接收 send() 发送的值给 task_id
                char_value = chr(ord(char_value) + 1)
                print(f"task_id:{task_id}")
                print(f"char_value:{char_value}")
            case _:
                task_id = yield # 返回 None
                print(f"task_id:{task_id}")

g = gen()
print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 注意:如果通过 send 启动生成器,第一次传递的值必须是 None,因为这个时候还没有 yield 表达式能够接收你传递的值
# print(g.send(None))
# print(g.send(0))
# print(g.send(1))
# print(g.send(1))
# print(g.send(0))
# print(g.send(1))
# print(g.send(2))
# print(g.send(3))
print("~~~~~~~~~~")
print(g.send(0))
print(g.send(0))
print(g.send(0))
print(g.send(0))

print(g.send(1))
print(g.send(1))
print(g.send(1))
print(g.send(1))
print(g.send(1))