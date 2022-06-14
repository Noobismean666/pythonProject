name = "小明"
age = 25
height = 180.5
str1 = "我叫" + name +", 今年" +str(age) + "岁，身高" + str(height)
print(str1)
str2 = "我叫{0},我在{1}班，今年{2},身高{3}".format(name,"3-2",age,height)
print(str2)
str3 = "我叫{p1},我在{p2}班，今年{p3},身高{p4}".format(p1=name,p2="3-2",p3=age,p4=height)

#数字的格式化
num = 1234567.89555
str4 = format(num , '0.4f')
print(type(str4))
print(str4)

account = "8810381"
amt = 123456789
str5 = format(amt,"0,.3f")
str6 = "请您向" + account +"账户转账¥" + str5 +"元"
print(str6)
#在字符串格式化输出时，如遇要格式化输出的数字，则需要在{}内增加：前缀，之后写上数字格式化语句
str7 = "请您向{}账户转账¥{:0,.3f}".format(account,amt)
print(str7)

#早期的字符串格式化
#我叫张三，今年30岁，体重87.5公斤
name = "张三"
age = 30
weight = 87.5
str8 = "我叫%s,今年%d岁，体重%.2f公斤"%(name,age,weight)
print(str8)
# 6-14
