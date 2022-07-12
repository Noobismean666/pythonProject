# 其他常用方法
persons = ['张三','赵六','李四','王五','赵六','钱七','孙八']

#统计出现次数
cnt = persons.count('赵六')
print(cnt)

#追加操作
#append将整个列表追加到末尾，extend则是将列表中的元素追加到原始列表末尾
persons.append(['杨九','吴十'])
print(persons)
persons.extend(['杨九','吴十'])
print(persons)

#in（成员运算符） 运算符用于判断数据是否在列表中存在，存在返回True，不存在返回False
persons.remove('张三')
b = '张三' in persons
print(b)

#copy 函数用于复制列表
persons1 = persons.copy()
persons2 = persons
print(persons1)
#is 身份运算符用于判断两个变量是否指向同一块内存
print(persons1 is persons)
print(persons2 is  persons)

# clear 用于清空列表
persons.clear()
print(persons)
print(persons1)
print(persons2)




list1 = [23,98,56,55,76,98,55]
# 定义list2为空列表
list2 = []
#循环遍历list1

for l in list1:
    if l not in list2:
        list2.extend([23,98,56,55,76,98,55])
        list2.sort(reverse=True)
print(list2)

#定义变量reason
reason = [[3,4,5],[6,7,8],[9,10,11],[12,1,2]]
# 变量month接收input函数“请输入1-12之间的月份，并将输入的数值转化为int()类型
month = input("请输入1-12之间的月份")
month = int(month)
# if判断month在嵌套的一个列表里
if month in reason[0]:
    print('{0}月是春季'.format(month))
# elif判断month在嵌套的第二个列表里，并像控制台输出时夏季
elif month in reason[1]:
    print('{0}月是夏季'.format(month))
elif month in reason[2]:
    print('{0}月是秋季'.format(month))
elif month in reason[3]:
    print('{0}月是冬季'. format(month))
else:
    print("您输入的月份有误！！")

