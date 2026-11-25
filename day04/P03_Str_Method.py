"""
    字符串常用函数
"""
# str1 = "abcdecccc"
# str.replace(old,new[,max])	把将字符串中的old替换成new,如果指定max，则替换不超过max次
# print(str1.replace("c", "*", 2))

# str1 = "a,b,c,d,e,f"
# str.split([x][,n])	按x分隔字符串，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数
# print(str1.split(",", 2))
# str.rsplit([x][,n])	与split()类似，从右边开始分隔
# print(str1.rsplit(",", 2))

# x.join(seq)	以x作为分隔符，将序列中所有的字符串合并为一个新的字符串
# print("_".join(["a", "b", "c"]))

# str1 = "   hello world   "
# str.strip([x])	截掉字符串两边的空格或指定字符
# print(str1.strip())
# str.lstrip([x])	截掉字符串左边的空格或指定字符
# print(str1.lstrip())
# str.rstrip([x])	截掉字符串右边的空格或指定字符
# print(str1.rstrip())

# str1 = "hello"
# str.removeprefix()	截掉字符串指定前缀
# print(str1.removeprefix("he"))
# str.removesuffix()	截掉字符串指定后缀
# print(str1.removesuffix("lo"))

# str1 = "hello"
# str.upper()	将所有字符转为大写
# print(str1.upper())
# str.lower()	将所有字符转为小写
# print(str1.upper().lower())


# str1 ="hEllo"
# str.swapcase()	反转字符串中字母大小写
# print(str1.swapcase())
# str.capitalize()	将字符串第一个字母变为大写，其他字母变为小写
# print(str1.capitalize())


# str1 = "hellO WorlD"
# str.title()	将字符串每个单词首字母大写
# print(str1.title())
# str.casefold()	返回适合无大小写比较的字符串版本
# print(str1.casefold())

# len(str)	返回字符串长度
# print(len(str1))
# max(str)	返回字符串中最大值
# print(max(str1))
# min(str)	返回字符串中最小值
# print(min(str1))

# str1 = "hello world"
# str.find(x[,start][,end])	返回字符串中第一个x的索引值，不存在则返回-1，可指定字符串开始结束范围
# print(str1.find("d"))
# str.rfind(x[,start][,end])	与find()类似，从右边开始查找
# print("abcdefbg".find("b"))
# print("abcdefbg".rfind("b"))

# str.index(x[,start][,end])	返回字符串中第一个x的索引值，不存在则报错，可指定字符串开始结束范围
# print(str1.index("z"))
# str.rindex(x[,start][,end])	与index()类似，从右边开始查找

# str.count(x[,start][,end])	返回字符串中x的个数，可指定字符串开始结束范围
# print("abbbcd".count("b"))

# str1 = "hello world"
# str.startswith(x[,start][,end])	检查字符串是否以x开头，可指定字符串开始结束范围
# print(str1.startswith("hel"))
# str.endswith(x[,start][,end])	检查字符串是否以x结尾，可指定字符串开始结束范围
# print(str1.endswith("dl"))

# str.isspace()	检查字符串是否非空且只包含空白
# print("  ".isspace())

str1 = "a_$1234"
# str.isalnum()	检查字符串是否非空且只包含字母(英文字母+汉字)和数字
# print(str1.isalnum())
# str.isalpha()	检查字符串是否非空且只包含字母(英文字母+汉字)
# print(str1.isalpha())
# str.isascii()	检查字符串是否只包含ASCII字符，空字符串也是ASCII
# print(str1.isascii())
# str.isdecimal()	检查字符串是否非空且只包含十进制字符
# print(str1.isdecimal())
# str.isdigit()	检查字符串是否非空且只包含数字
# print(str1.isdigit())
# str.isidentifier()	检查字符串是否是有效的标识符
print(str1.isidentifier())