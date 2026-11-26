"""
    演示了文件的copy
"""
"""
# 需求:将C:\\Users\\13126\\Pictures\\电脑壁纸\\暗色系\\6712dd76a01dad926cb3580ba901be7b.jpg 拷贝到当前目录
def copy_file(src, dest):
    # 图片形式,以二进制模式读取
    # 打开源文件
    src_file = open(src, "rb")
    # 将源文件内容读取到程序中
    content = src_file.read()

    # 打开目标文件
    dst_file = open(dest, "wb")
    # 将读取到的数据写入到目标文件
    dst_file.write(content)
    
    # 关闭文件
    dst_file.close()
    src_file.close()

src = "C:\\Users\\13126\\Pictures\\电脑壁纸\\暗色系\\6712dd76a01dad926cb3580ba901be7b.jpg"
dest = "./be7b.jpg"
copy_file(src, dest)
"""

# 优化版本
def copy_file(src, dest):
    # 打开源文件
    src_file = open(src, "rb")
    # 打开目标文件
    dst_file = open(dest, "wb")

    # 从源文件中读取数据到程序中
    # content = src_file.read(1024)
    # while content:
    #     # 将读取到的数据写入到目标文件中
    #     dst_file.write(content)
    #     content = src_file.read(1024)

    while content := src_file.read(1024):
        dst_file.write(content)

    # 关闭文件
    src_file.close()
    dst_file.close()

src = "C:\\Users\\13126\\Pictures\\电脑壁纸\\暗色系\\6712dd76a01dad926cb3580ba901be7b.jpg"
dest = "./be7b2.jpg"
copy_file(src, dest)