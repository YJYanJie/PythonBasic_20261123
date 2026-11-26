"""
    演示了读写文件操作
    r 只读,文件若不存在则会报错,默认此模式
    w 覆盖写入,文件不存在会创建文件
    a 追加写入,在原有数据后追加,文件不存在则会创建新文件
    x 创建新文件并写入,若文件已存在则会报错
    b 以二进制模式打开,一般用于非文本如图片等
    t 以文本模式打开,默认此模式
    + 能读能写
"""
"""
# -----向磁盘文件中写入数据-----
# 建立连接(open方法打开文件)
file = open("test.txt", "w")
# print(type(file))

# 写入数据
file.write("hello world\n")
file.write("nihao python\n")

# 关闭连接
file.close()
"""
"""
# -----从磁盘文件中读取数据-----
# 打开文件
file = open("test.txt", "rt")

# 读取数据 -- read()
# read() 没有加任何参数,表示读取文件中所有内容
# read(size) 如果加参数,表示从文件读取的字符 | 字节数
# print(file.read())
# print(file.read(3))
# print(file.read(5))
# print(file.read(8)) # 会持续读取文件内容

# 读取数据 -- readline() 读取一行数据
# print(file.readline())
# print(file.readline())

# 读取数据 -- readlines()
# print(file.read())
print(file.readlines())

# 关闭文件
file.close()
"""

# 获取当前目录的所有内容
import os

# os.walk() 递归遍历目录
# os.getcwd() 获取当前路径
for root, dirs, files in os.walk("../"):
    # print(item)
    print("当前路径：", root)
    print("目录：", dirs)
    print("文件：", files)
    print()