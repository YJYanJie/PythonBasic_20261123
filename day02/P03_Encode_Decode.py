"""
    演示了字符的编码以及解码
"""

str1 = "你好中国"
print(str1)
# 编码: 将字符串转换为字节的过程
b1 = str1.encode(encoding="gbk")
print(b1, type(b1))

print("~" * 20)
# 解码: 将字节数据转换为字符串的过程
str2 = b1.decode(encoding="gbk")
print(str2, type(str2))

# 注意: 编码和解码的时候,encoding 需要保持一致
