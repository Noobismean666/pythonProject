#遍历列表

persons = ['张三','赵六','李四','王五','赵六','钱七','孙八']

count = len(persons)#获取列表长度
print(count)
#for循环用于遍历列表
#for 迭代变量 in 可迭代对象


i = 0
for p in persons:
    if p == '赵六':
       ri = count * -1 + i
       print(p,i,ri)
    i += 1
'''
i = 0
while i < len(persons):
    p = persons[i]
    if p == '赵六':
        ri = count * -1 + i
        print(p,i,ri)
    i += 1
'''

'''
numList = [1,2,3,4,5,6,7,8,9,10]

b = 1
o = 0
for n in numList:
    if n % 2 == 0:
        print(n,b)
        b += 1
    o += 1
'''