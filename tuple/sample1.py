# 元组的使用
# 创建
t = ('a','b','c',1,2,3)
print(t)
print(type(t))

# 获取数据，在获取数据时与列表完全相同
print(t[5]) # 正序索引，获取第6个元素
print(t[-1]) # 倒序索引
print(t[1:4]) # 范围取值
print('b'in t) # 成员运算符
# 元组在创建后内容不可变
# t[0] = 2
# 写入数据的函数同样不被支持
# t.insert('f')
# 如果元组内持有列表，那么列表的内容是允许被修改的
t2 = (['张三',38,5000],['李四',28,2000])
item = t2[0]
print(item)
item[1] = 40
print(t2)
# t2.pop(0)

# 元组运算符
# 元组运算符同样适用于列表
t3 = (1,2,3) + (4,5,6)
t6 = (1,2,3) + (4,5,6)
print(t3)
print(t6)
# 如果元组只有一个元素时，必须在这个元素后增加逗号说明这是一个元组
t4 = ('see',)*2
print(t4)

