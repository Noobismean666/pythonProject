# #字符串的创建
# str1 = "Hello World!"
# str2 = 'Nice to meet you'
# str3 = "I told my friend""she is beautiful"
# str4 = "my dog's name is andy"
# #字符串的拼接
# str5 = str1 + str2
# print(str5)
# #文本转数字 ：int() float()
# #数字转文本 ：str()
# str6 ="MF" + str(8675)
# print(str6)

# 定义变量strText进行赋值
# strText = "Hello"
# # 定义一个int型变量strInt，赋初始值2020
# strInt = int(2020)
# # 进行字符串的拼接
# resultStr = strText + str(strInt)
# print("拼接后的字符串为 ："+resultStr)
#
# # 定义变量date,接收input函数-请输入日期：
# date = input("请输入日期")
# str1 = "Welcom to imooc"
# str2 = "  Imocc's URL is https://www.imocc.com/"
# #定义变量str3拼接date，str1,str2
# str3 = date + str1 +str2
# print(str3)


#大小写转换、
str7 = "bmw"
print(str7.upper())
print("bmw".upper()) # 转换为大写
print("BMW".lower()) # 转换为小写
print("how are you".capitalize()) # 首字母大写
print("michael jackson".title()) #title()设置每个单词首字母大写
print("abcDEF".swapcase()) #大小写互换

#制表符与换行符
table = "姓名\t性别\t年龄\n赵四\t男士\t42"
print(table)

#删除空白
space_str = "   hello world   "
print(space_str)
#len()用于获取字符串的长度
lstr = len(space_str)
print(lstr)
nospace_str = space_str.strip()
print(nospace_str)
print(len(nospace_str))

str1 = "  imocc    "
# 定义变量lenStr，存放字符串长度
lenStr = len(str1)
# 根据效果图输出字符串的长度
print("字符串长度：" , lenStr)
# 定义变量strC，存放去掉左右空白的字符串
strC = str1.strip()
print("去除空白后的字符串",strC)
# 根据效果图去掉空白后的字符串及字符串的长度进行输出
print("去除空白后字符串的长度",len(strC))

# 字符串查找
source = "Nice to meet you, i need your help!"
index = source.find("ee")
print(index)

isexist = "ee" in source
print(isexist)

# 字符串替换
str8 = "this is string example..wow!! this is really string"
pstr8 = str8.replace("is","was")
print(pstr8)
pstr8 = str8.replace("is","was",3)
print(pstr8)

Str = "imooc"
str9 = Str.replace("o","i")
print(str9)
str10 = Str.replace("o","i",1)
print(str10)
# 6-14