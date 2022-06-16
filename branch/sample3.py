a = 4 > 1 #True
b = 5 < 2 #False
c = 8 == 8 #True
d = 9 < 6 #False

print(a and b ) #False
print(a and c)#True
print(a or b)#True
print(b or d)#False
print(not a)#True
print(not b)#True
#逻辑运算符优先级为 not > and > or
r1 = a and b or c and not d
# a and b or c and True
# False or True
# True
print(r1)

r2 = (a and (not b or c) and d)
#(a and (True or c)) and d
#(a and True) and d
#True and d
#False
print(r2)

#定义变量year，并接收“请输入正确的年份：”
year = int(input("请输入正确的年份："))
#判断是否是闰年：1.能被4整除，但是不能被100整除的年份  2.能被400整除的年份
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))