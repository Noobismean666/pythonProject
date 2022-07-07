#成员运算符
sheet = {'张三','李四','王五'}
if('张三'in sheet):
    print("张三在听课")
else:
    print("张三已旷课")


#身份运算符
a = 5
b = a
c = 5.0
print(a is b)
print(a == c) # 数值进行比较
print(a is c) # 内存地址比较


str1 = "2020 "
str2 = "2020"
print(str1 == str2)
print(str1 is str2)


